from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

try:
	from tools.release import (
		ReleaseEntry,
		bump_next_version,
		check_versions,
		format_commit_subject,
		git_command,
		next_patch,
		read_latest_release,
	)
except ModuleNotFoundError:
	from release import (
		ReleaseEntry,
		bump_next_version,
		check_versions,
		format_commit_subject,
		git_command,
		next_patch,
		read_latest_release,
	)


ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class ReleasePlan:
	bump: bool
	title: str


def main() -> int:
	args = parse_args()
	validate_versions()
	current = read_latest_release(ROOT)
	default_subject = format_commit_subject(current)

	print(f"\n  Changelog version: {current.version}")
	print(f"  Commit subject:    {default_subject}")
	file_count = show_status()
	if args.dry_run:
		version, subject = preview_release(args, current)
		print(render_review(file_count, subject, version))
		print("  Dry run only. No version, pull, stage, commit, or push change was made.\n")
		return 0

	print(render_review(file_count, default_subject, current.version))
	version_snapshot = capture_release_files()
	bump_pending = False
	try:
		plan = select_release_plan(args)
		if plan.bump:
			result = bump_next_version(ROOT, plan.title)
			bump_pending = True
			current = read_latest_release(ROOT)
			default_subject = format_commit_subject(current)
			print(f"\n  Bumped {result.current_version} -> {result.next_version}")
			print(f"  Commit subject: {default_subject}\n")

		subject = args.message or ask(
			f"  Commit message [{default_subject}]: ", default_subject
		).strip() or default_subject
		validate_versions()
		file_count = len(status_lines())
		if not file_count:
			raise RuntimeError("There are no changes to commit.")
		confirm_mutation(subject, current.version, file_count)
		bump_pending = False
		check_and_pull()
		print("  > git add -A")
		run_git("add", "-A")
		print(f'  > git commit -m "{subject}"')
		run_git("commit", "-m", subject)
		print("  > git push")
		run_git("push")
		print(f"\n  Done - {subject}\n")
	except Exception:
		if bump_pending:
			restore_release_files(version_snapshot)
		raise
	return 0


def preview_release(args: argparse.Namespace, current: ReleaseEntry) -> tuple[str, str]:
	if not args.bump:
		return current.version, format_commit_subject(current)
	version = next_patch(current.version)
	return version, f"#{int(version.split('.')[2])} - {args.title}"


def select_release_plan(args: argparse.Namespace) -> ReleasePlan:
	if args.bump:
		return ReleasePlan(True, args.title)
	if args.no_bump:
		return ReleasePlan(False, args.title)
	answer = ask("  Bump next version before commit? [y/N]: ")
	if not is_yes(answer):
		return ReleasePlan(False, args.title)
	title = ask("  Version title [version update]: ", "version update").strip() or "version update"
	return ReleasePlan(True, title)


def confirm_mutation(subject: str, version: str, file_count: int) -> None:
	print(render_review(file_count, subject, version))
	if not is_yes(ask("  Continue with pull, stage, commit, and push? [y/N]: ")):
		raise RuntimeError("Cancelled.")


def capture_release_files() -> dict[Path, bytes]:
	files = [ROOT / "logicx_ishop/__init__.py", ROOT / "assist/documentation/CHANGELOG.md"]
	return {file: file.read_bytes() for file in files}


def restore_release_files(snapshot: dict[Path, bytes]) -> None:
	for file, content in snapshot.items():
		file.write_bytes(content)


def check_and_pull() -> None:
	upstream = run_git_quiet("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}")
	if not upstream:
		print("\n  No upstream branch found. Skipping pull.\n")
		return
	print("\n  > git fetch")
	run_git("-c", "maintenance.auto=false", "-c", "gc.auto=0", "fetch", "--quiet")
	behind = int(run_git_quiet("rev-list", "--count", f"HEAD..{upstream}") or "0")
	if not behind:
		print("  Already up to date.\n")
		return
	print(f"  Branch is behind {upstream} by {behind} commit(s).")
	print("  > git pull --rebase --autostash")
	run_git("-c", "maintenance.auto=false", "-c", "gc.auto=0", "pull", "--rebase", "--autostash")


def validate_versions() -> None:
	version, failures = check_versions(ROOT)
	if failures:
		details = "\n".join(f"- {failure}" for failure in failures)
		raise RuntimeError(f"Version check failed for {version}:\n{details}")
	print(f"Version check passed for {version}.")


def show_status() -> int:
	files = status_lines()
	print(f"  Uncommitted: {len(files)} files\n")
	for file in files:
		print(f"    {file}")
	if files:
		print()
	return len(files)


def status_lines() -> list[str]:
	status = run_git("status", "--porcelain", capture=True)
	return [line for line in status.splitlines() if line]


def render_review(file_count: int, subject: str, version: str) -> str:
	rows = ["GitHub Commit Review", f"Version: {version}", f"Subject: {subject}", f"Files: {file_count}"]
	width = max(len(row) for row in rows) + 4
	border = f"+{'-' * width}+"
	body = [f"| {row.ljust(width - 2)} |" for row in rows]
	return "\n".join(["", border, *body, border, ""])


def ask(question: str, default: str = "") -> str:
	if sys.stdin.isatty():
		return input(question) or default
	if os.name == "nt":
		return ask_windows(question, default)
	raise RuntimeError("Interactive input is required. Run this command in a terminal.")


def ask_windows(question: str, default: str) -> str:
	if question.rstrip().endswith("[y/N]:"):
		message = question.rsplit("[y/N]:", 1)[0].strip()
		script = (
			"Add-Type -AssemblyName System.Windows.Forms; "
			f"$result = [System.Windows.Forms.MessageBox]::Show({powershell_quote(message)}, "
			"'GitHub Commit Review', 'YesNo', 'Question'); "
			"if ($result -eq 'Yes') { 'yes' } else { 'no' }"
		)
	else:
		script = (
			"Add-Type -AssemblyName Microsoft.VisualBasic; "
			f"[Microsoft.VisualBasic.Interaction]::InputBox({powershell_quote(question)}, "
			f"'GitHub Commit Review', {powershell_quote(default)})"
		)
	return subprocess.check_output(
		["powershell.exe", "-NoProfile", "-STA", "-Command", script],
		cwd=ROOT,
		text=True,
	).strip()


def powershell_quote(value: str) -> str:
	return f"'{value.replace(chr(39), chr(39) * 2)}'"


def is_yes(value: str) -> bool:
	return value.strip().lower() in {"y", "yes"}


def run_git(*args: str, capture: bool = False) -> str:
	result = subprocess.run(
		git_command(ROOT, *args),
		cwd=ROOT,
		text=True,
		capture_output=capture,
		check=True,
	)
	return result.stdout.strip() if capture else ""


def run_git_quiet(*args: str) -> str:
	try:
		return run_git(*args, capture=True)
	except subprocess.CalledProcessError:
		return ""


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Review and publish the current LogicX iShop changes.")
	parser.add_argument("--dry-run", action="store_true")
	bump_group = parser.add_mutually_exclusive_group()
	bump_group.add_argument("--no-bump", action="store_true")
	bump_group.add_argument("--bump", action="store_true")
	parser.add_argument("--title", default="version update")
	parser.add_argument("--message")
	return parser.parse_args()


if __name__ == "__main__":
	try:
		raise SystemExit(main())
	except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
		print(f"\n  Error: {error}\n", file=sys.stderr)
		raise SystemExit(1) from None

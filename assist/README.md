# LogicX iShop Assist Pack

This folder is the working guide for developers and AI agents.

Read these files before changing the application:

1. `assist/AGENT-GUIDE.md`
2. `assist/agents/agent-rules.md`
3. `assist/SKILL.md` for Frappe development work
4. `assist/documentation/CHANGELOG.md` for release state

Use `assist/skills/frappe-framework.md` when a task changes Frappe behavior.

For TypeScript or JavaScript work, also read the relevant CXApp Assist files at `../cxapp/assist`.

Use CXApp only for TypeScript structure, lint, formatting, tests, and frontend quality patterns.

Do not copy CXApp business modules, tenant architecture, database ownership, or API design into this Frappe app.

## Release commands

Use these commands from the repository root.

## Show the current version

```powershell
python tools/version.py show
```

This command reads the version from `logicx_ishop/__init__.py`.

## Check version consistency

```powershell
python tools/version.py check
```

Run this command before a release. It checks the Python version and changelog metadata.

## Create the next patch version

```powershell
python tools/version.py bump --title "Version update"
```

This command creates the next patch version. It also adds a new changelog section.

Replace `Version update` with a short release title when the change has a specific purpose.

Review all changed files after the command completes.

## Preview the GitHub workflow

```powershell
python tools/github_now.py --dry-run
```

This command previews the current version, commit subject, and changed file count.

The dry run does not pull, stage, commit, or push changes.

Use `--dry-run --bump` to preview the next patch version without changing files.

Always run the dry run before the interactive GitHub workflow.

Do not stage, commit, pull, or push without the user's final approval.

## Required release order

1. Show the current version.
2. Check version consistency.
3. Create a patch version when the release needs one.
4. Check version consistency again.
5. Run the GitHub dry run.
6. Review the version, subject, and changed files.
7. Ask for final approval before any Git mutation.

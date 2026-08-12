---
name: logicx-ishop-frappe-development
description: Develop, review, migrate, test, and release the LogicX iShop Frappe application.
---

# LogicX iShop Frappe Development

## Use this skill

Use this skill for DocTypes, controllers, hooks, permissions, APIs, patches, fixtures, jobs, tests, Bench, and releases.

## Start

1. Read `assist/AGENT-GUIDE.md`.
2. Read `assist/agents/agent-rules.md`.
3. Inspect Git status.
4. Inspect the owning DocType or feature files.
5. Confirm the Bench root and explicit site before a live command.

## Select the Frappe reference

Read `assist/skills/frappe-framework.md` for the task routing table and official source links.

Read only the sections that apply to the task.

## Implement

- Keep fields and permissions in DocType JSON.
- Keep lifecycle rules in the Python controller.
- Keep remote methods small and permission-aware.
- Keep hooks active and intentional.
- Keep patches ordered and immutable after release.
- Add focused tests for changed behavior.
- Preserve unrelated worktree changes.

If the task adds TypeScript or substantial JavaScript, read the relevant guide under `../cxapp/assist`.

## Verify

Use an explicit site for live checks:

```bash
bench --site <site> list-apps
bench --site <site> migrate
bench --site <site> run-tests --app logicx_ishop
bench build --app logicx_ishop
```

Run only the commands required by the change.

Do not claim database, browser, queue, or deployment proof from static checks.

## Release

```powershell
python tools/version.py show
python tools/version.py check
python tools/github_now.py --dry-run --no-bump
```

Use the patch bump command only when the release needs a new patch version.

```powershell
python tools/version.py bump --title "Version update"
```

Do not perform Git mutations without final user approval.

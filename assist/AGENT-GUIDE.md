# LogicX iShop Agent Guide

## Purpose

This guide applies to every developer and AI agent that changes LogicX iShop.

Read this file before planning, editing, reviewing, testing, migrating, or releasing the application.

The current source tree and Git state have priority over stale documentation.

## Required reading

Read these files for every change:

1. `assist/AGENT-GUIDE.md`
2. `assist/agents/agent-rules.md`
3. The closest application files

Read these files when relevant:

- Frappe work: `assist/SKILL.md`
- Framework rules: `assist/skills/frappe-framework.md`
- Release work: `assist/README.md`
- Version history: `assist/documentation/CHANGELOG.md`
- TypeScript work: the relevant guide under `../cxapp/assist`

Do not load unrelated planning or historical documents.

## Repository identity

- The application package is `logicx_ishop`.
- The application title is `LogicX iShop`.
- The primary module is `LogicX iShop`.
- The canonical repository is `https://github.com/CODEXSUN/logicx-ishop.git`.
- The Python package version is the release version source.
- ERPNext records can be linked only through declared Frappe contracts.

Do not add TM Shop, Trades, or another application identity to active code or documentation.

## Frappe ownership

Keep each DocType inside its owning Frappe module.

A complete DocType change can include these files:

```text
logicx_ishop/logicx_ishop/doctype/{doctype}/{doctype}.json
logicx_ishop/logicx_ishop/doctype/{doctype}/{doctype}.py
logicx_ishop/logicx_ishop/doctype/{doctype}/{doctype}.js
logicx_ishop/logicx_ishop/doctype/{doctype}/test_{doctype}.py
```

The DocType JSON owns fields, naming, indexes, permissions, and standard metadata.

The Python controller owns validation and document lifecycle behavior.

Client scripts can improve interaction. They must not be the only place for business validation.

Tests belong with the owned DocType or the feature that they verify.

## Data and migration rules

- Enable developer mode before saving DocType schema changes.
- Commit each generated DocType JSON change with its controller change.
- Add ordered data patches to `logicx_ishop/patches.txt`.
- Keep applied patches immutable.
- Make every patch safe to rerun when practical.
- Use Frappe document APIs for lifecycle-aware writes.
- Use direct database writes only when hooks must not run.
- Do not call `frappe.db.commit()` inside normal request code.
- Run `bench --site <site> migrate` after schema, hook, fixture, or scheduler changes.

Never describe a static JSON check as a successful database migration.

## Permission and API rules

- Define default DocType permissions in the DocType JSON.
- Use real roles that the installed application provides.
- Check permissions on custom reads and writes.
- Do not use `frappe.get_all` for user-scoped data without an approved reason.
- Whitelist only methods that require remote access.
- Use `GET` for read-only methods.
- Use `POST` for methods that change state.
- Validate all remote method inputs on the server.
- Do not expose secrets, internal exceptions, or unrestricted database queries.

## Hook and background job rules

- Keep `hooks.py` limited to active application integration.
- Remove unused generated hook examples when they cause confusion.
- Prefer controller methods for behavior owned by one DocType.
- Use hooks for cross-cutting integration with a clear owner.
- Enqueue long work instead of blocking a web request.
- Use `enqueue_after_commit=True` when a job depends on committed request data.
- Make retryable jobs idempotent.
- Run a migration after scheduler hook changes.

## TypeScript and JavaScript rules

Frappe remains the application framework and source of business behavior.

When TypeScript or JavaScript is added, read the relevant CXApp Assist guide at `../cxapp/assist`.

Reuse these CXApp practices:

- Strict TypeScript.
- Explicit domain types.
- Boundary validation.
- ESLint and Prettier checks.
- Small module-owned files.
- Loading, empty, error, and permission states.
- Tests for important interaction states.

Do not reuse CXApp tenant, Fastify, React, workspace, or database architecture unless the user approves a separate integration.

## Verification order

Run checks that match the change:

1. Inspect Git status and preserve unrelated changes.
2. Compile changed Python files.
3. Validate changed JSON files.
4. Run Ruff, ESLint, Prettier, or pre-commit checks when configured.
5. Run focused Frappe tests on an explicit site.
6. Run `bench --site <site> migrate` for database changes.
7. Build application assets when frontend assets change.
8. Check the application in Desk or the browser when interaction changes.
9. Run the version checker before release work.
10. Run the GitHub dry run before any Git mutation.

Report each check that ran. Report each unavailable live check as unavailable.

## Git and release safety

- Preserve unrelated worktree changes.
- Do not stage, commit, pull, push, tag, or publish without final user approval.
- Run `python tools/github_now.py --dry-run --no-bump` before a current-version release.
- Run `python tools/github_now.py --dry-run` before a patch-bump release.
- Review the version, subject, and changed file count.
- Update `assist/documentation/CHANGELOG.md` with each release.

## Completion report

State the outcome first.

Then report changed ownership, database impact, checks that passed, skipped checks, and remaining blockers.

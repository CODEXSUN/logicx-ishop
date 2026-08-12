# LogicX iShop Agent Rules

## Mandatory behavior

- Read `assist/AGENT-GUIDE.md` before changing the repository.
- Read `assist/SKILL.md` for every Frappe feature or lifecycle change.
- Inspect the live tree and Git status before editing.
- Preserve unrelated user changes.
- Use the current source as the primary implementation record.
- Make the smallest complete change that satisfies the request.
- Record assumptions that change product behavior.
- Keep documentation synchronized with active behavior.

## Framework rules

- Use Frappe and Bench for application lifecycle operations.
- Run Bench commands from a Bench root.
- Pass `--site <site>` to every site command.
- Never run a bare migration against an unknown site.
- Do not create DocType folders by hand in an active developer site workflow.
- Do not bypass controller validation for convenience.
- Do not trust client-side validation as a permission boundary.
- Do not add a whitelisted method without server input and permission checks.
- Do not use manual database commits in normal request handlers.

## Review rules

Reviewers must check:

- DocType fields and naming match the business purpose.
- Link fields point to installed or declared dependencies.
- Roles in permission rows exist.
- Controller validation covers server-side writes.
- Delete, submit, cancel, and rename behavior is intentional.
- Queries respect Frappe permissions.
- Background jobs can retry safely.
- Migrations preserve existing data.
- Tests cover the changed lifecycle and permission behavior.
- Documentation and versions match the source.

## TypeScript rule

Read the relevant CXApp Assist file before changing TypeScript or JavaScript architecture.

Use CXApp as a language and quality reference only.

Do not copy CXApp application ownership into LogicX iShop.

## Destructive operations

Back up a site before an uninstall, destructive patch, or risky schema conversion.

Resolve the exact site and DocType before deleting data.

Do not remove Docker volumes, sites, databases, or files without explicit approval.

## Release rule

Always run the GitHub dry run first.

Do not stage, commit, pull, push, tag, or publish without final approval.

Report the exact release version and commit subject before asking for approval.

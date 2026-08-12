# Changelog

Current version: 1.0.2
Release tag: v-1.0.2
Changelog label: v 1.0.2

## v-1.0.2

### [v 1.0.2] 2026-08-12 6:21 pm - Version update

#### Database Changes

- Database update: No (auto-check).

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.2.
- Aligned the GitHub workflow preview and prompts with CXApp.
- Changed the default dry run to review the current changelog version without a bump.
- Added an explicit `--dry-run --bump` preview for the next patch version.
- Restored version and changelog files when a user cancels an uncommitted bump.
- Added exact changelog metadata checks and latest-entry version validation.

## v-1.0.1

### [v 1.0.1] 2026-08-12 - Initial LogicX iShop release

#### Database Changes

- Database update: Yes.
- Added the iShop Item and iShop Catalog DocTypes.
- Added the Catalog Item child table.

#### App Codebase Changes

- Set the LogicX iShop application version to 1.0.1.
- Added Python tools for version checks, patch bumps, and changelog entries.
- Added a reviewed Git pull, commit, and push workflow.
- Added native Bench release commands.

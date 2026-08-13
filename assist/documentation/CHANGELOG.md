# Changelog

Current version: 1.0.4
Release tag: v-1.0.4
Changelog label: v 1.0.4

## v-1.0.4

### [v 1.0.4] 2026-08-13 7:52 am - CXShop catalog integration contract

#### Database Changes

- Database update: Yes (auto-check).

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.4.

## v-1.0.3

### [v 1.0.3] 2026-08-12 - CXShop catalog integration contract

#### Database Changes

- Database update: Yes. Replaced legacy TM DocType permissions with LogicX iShop User and LogicX
  iShop Manager roles, while retaining explicit System Manager integration access.
- Migrated both `tmshop.localhost` and the isolated `tmshop-test.localhost` sites and seeded the
  deterministic `CXSHOP-DEMO-*` catalog through the API.

#### App Codebase Changes

- Connected LogicX iShop to the Frappe v16 Desk through an app-level Desktop Icon that is visible to all Desk users and opens the iShop Catalog.
- Added renamed light and dark LogicX iShop logo assets and connected the light logo to the Desk icon, app screen, and reinstall hook.
- Added an app-owned LogicX iShop Workspace Sidebar with package and catalog icons instead of Frappe's generic DocType list icons.
- Moved ERPNext Item to the top of the iShop Item form and added permission-aware form autofill for item identity, descriptions, selling price, image, and highlights.
- Kept ERPNext Item optional so iShop Items can also be entered independently.
- Added permission-aware snapshot, batch upsert, and demo-seed methods for ERPNext Item, iShop Item,
  iShop Catalog, and Catalog Item child records.
- Added an integration test covering all four catalog layers on the isolated Frappe test site.
- Expanded the idempotent demo catalog to 50 computer-related ERPNext and iShop items with images,
  prices, brands, highlights, and 10 category catalogs for live CXShop posting.
- Made demo Item, iShop Item, and iShop Catalog descriptions provider-neutral so the same business
  content remains correct when CXShop switches between its local database and Frappe.

### [v 1.0.3] 2026-08-12 7:19 pm - Version update

#### Database Changes

- Database update: Yes (manual).
- Added a standard Desktop Icon export for LogicX iShop.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.3.
- Added the LogicX iShop Desk desktop icon record with module routing and app roles.

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

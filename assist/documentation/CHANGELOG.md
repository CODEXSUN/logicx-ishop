# Changelog

Current version: 1.0.7
Release tag: v-1.0.7
Changelog label: v 1.0.7

## v-1.0.7

### [v 1.0.7] 2026-08-13 6:02 pm - Item iShop tab and unique ERPNext Item link

#### Database Changes

- Database update: Yes (auto-check).
- Added the `ishop_tab` Tab Break and `ishop_item_details_html` HTML Custom Fields to ERPNext Item
  through `after_install` and the `logicx_ishop.patches.add_item_ishop_tab` patch.
- Made `iShop Item.erpnext_item` unique, which adds a unique index on `tabiShop Item`. The
  pre-model-sync patch `logicx_ishop.patches.validate_unique_erpnext_item` stops the migration with
  the offending item codes when a site still holds duplicate links.
- Run `bench --site <site> migrate` and `bench build --app logicx_ishop` on each site.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.7.
- Added an iShop tab to the ERPNext Item form that lists the linked iShop Item with its code, name,
  availability, item group, brand, web price, MRP, published state, highlights, short description,
  image, and last update.
- Added the permission-aware `logicx_ishop.custom.item.get_linked_ishop_items` read method and served
  the tab through the `doctype_js` hook for Item.
- Added distinct tab states for an unsaved Item, a missing iShop Item link, a missing iShop Item read
  permission, and a failed load.
- Showed the Create iShop Item button only when the Item has no linked iShop Item and the user holds
  create permission, and opened the new form with ERPNext Item prefilled.
- Styled the Open iShop Item button with a black background.
- Limited each ERPNext Item to one iShop Item through the unique field and a readable controller
  validation.
- Stopped copying Full Description and Highlights from the ERPNext Item so both stay author-owned.
- Added tests for the Item custom fields, linked and unlinked reads, rejected item names, the single
  link rule, and the fields that are never autofilled.

## v-1.0.6

### [v 1.0.6] 2026-08-13 11:40 am - Desktop icon rename to iShop LogicX

#### Database Changes

- Database update: Yes (manual).
- Renamed the standard Desktop Icon record from `LogicX iShop` to `iShop LogicX`. A migration
  inserts the renamed record, so remove the stale `LogicX iShop` Desktop Icon on each existing site.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.6.
- Renamed the Desktop Icon export from `desktop_icon/logicx_ishop.json` to
  `desktop_icon/ishop_logicx.json` so the file name matches the record name.
- Changed the Desktop Icon `name` and `label` to `iShop LogicX`.
- Kept the Desktop Icon pointed at `/app/ishop-catalog`.

## v-1.0.5

### [v 1.0.5] 2026-08-13 8:10 am - Fix release tool package conflict

#### Database Changes

- Database update: No (auto-check).

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.5.
- Loaded release helpers from the repository's exact `tools/release.py` path and removed the top-level `tools` package marker to prevent conflicts with other Frappe apps.

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

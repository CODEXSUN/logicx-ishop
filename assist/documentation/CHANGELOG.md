# Changelog

Current version: 1.0.15
Release tag: v-1.0.15
Changelog label: v 1.0.15

## v-1.0.15

### [v 1.0.15] 2026-08-20 5:39 pm - Item Statistics column widths

#### Database Changes

- Database update: No (auto-check).

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.15.
- Narrowed the `Item Group` column of the `Item Statistics` report from 300 to 250 and the `Brand`
  column from 250 to 150, so the count column is read without scrolling the report.

## v-1.0.14

### [v 1.0.14] 2026-08-20 5:33 pm - Item Statistics sidebar link

#### Database Changes

- Database update: Yes (manual).
- Updated the standard `LogicX iShop` Workspace Sidebar record, which is synced on migrate. No table
  or field changes, so the stored data is untouched.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.14.
- Added the `Item Statistics` query report link to the `LogicX iShop` workspace sidebar, so the report
  is opened from the sidebar instead of the report list.

## v-1.0.13

### [v 1.0.13] 2026-08-20 1:37 pm - Item Statistics report

#### Database Changes

- Database update: Yes (manual).
- Added the `Item Statistics` standard Report record for the `iShop Item` DocType, inserted on
  migrate. No table or field changes, so the stored data is untouched.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.13.
- Added the `Item Statistics` script report under `logicx_ishop/logicx_ishop/report/item_statistics`,
  along with the new `report` package, so iShop Item coverage can be reviewed without exporting the
  list view.
- Reported one row per Item Group and Brand pair with the matching iShop Item count, ordered by count
  descending, with a total row.
- Added the mandatory `Type` filter with the Published, Non-Published, Image Set, Image Not Set,
  Price Set, Price Not Set, and All Items options, defaulting to Published. Price Set and Price Not
  Set read `web_price`, and All Items counts every iShop Item.
- Labelled the count column with the selected Type, so the column header reads Published, Image Not
  Set, or whichever option is in use.
- Granted the report to the `System Manager`, `TM Admin`, `TM User`, and `LogicX iShop Manager` roles.

## v-1.0.12

### [v 1.0.12] 2026-08-17 1:20 pm - ERPNext autofill on creation only

#### Database Changes

- Database update: Yes (auto-check).
- Added the `Not Available` option to the `availability` Select field on iShop Item, so an item can be
  marked as out of stock. Existing values stay valid.
- Moved the `highlights` field above the `details_column` Column Break on iShop Item, so Highlights
  now closes the first column of the details section instead of opening the second.
- Added the `TM User`, `TM Admin`, `LogicX iShop Manager`, and `System Manager` roles to the
  `iShop LogicX` Desktop Icon, so the icon is shown to those roles instead of every Desk user.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.12.
- Restricted the ERPNext Item autofill in `before_validate` to new documents through `is_new()`, so a
  field that the author clears on an existing iShop Item is no longer refilled on the next save.
- Stopped copying Web Price from the ERPNext Item and removed the `_selling_price` helper, so the
  iShop web price stays author-owned like Full Description and Highlights.

## v-1.0.11

### [v 1.0.11] 2026-08-15 5:12 pm - iShop Item image preview

#### Database Changes

- Database update: Yes (auto-check).
- Added the `image_preview` HTML field to iShop Item, placed between `highlights` and `image` in the
  second column of the details section. The field stores nothing, so no stored data changes.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.11.
- Added an image preview above the Image field on the iShop Item form, so the attached image is
  visible without opening the file.
- Rendered the preview at the full width of the details column, capped at 70% of the viewport height
  and fitted with `object-fit: contain`, so the image stays as large as the column allows without
  distortion or overflow.
- Hid the preview when the iShop Item has no image, so the form keeps its layout.
- Redrew the preview on form refresh and on every change of the Image field, including the image that
  the ERPNext Item autofill sets.

## v-1.0.10

### [v 1.0.10] 2026-08-15 4:35 pm - iShop Item form layout

#### Database Changes

- Database update: Yes (auto-check).
- Re-laid out the iShop Item form with three new layout fields: the `details_section` Section Break,
  the `details_column` Column Break, and the `description_section` Section Break. The stored data is
  untouched, since only the field order and the layout fields change.
- Restricted the `Catalog Item.ishop_item` link to published iShop Items through the `link_filters`
  property, so the link search no longer offers unpublished items.
- Run `bench --site <site> migrate` on each site.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.10.
- Grouped the iShop Item identity, classification, and price fields in the first column of the details
  section: ERPNext Item, Item Code, Item Name, Availability, Item Group, Brand, Web Price, and MRP.
- Moved Highlights, Image, and Published into the second column of the details section, so the image
  and its publish state sit beside the item details.
- Moved Short Description and Full Description into their own full-width section below the details.
- Left both section breaks unlabelled, so the form keeps the layout without extra headings.

## v-1.0.9

### [v 1.0.9] 2026-08-14 6:25 pm - Open iShop Item button beside the image

#### Database Changes

- Database update: No (auto-check).

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.9.
- Moved the Open iShop Item button out of the card header and placed it next to the iShop Item image
  on the ERPNext Item iShop tab.
- Kept the card title on its own line and aligned the image and the button in one centered row with a
  small gap, so the button stays beside the image and starts the row when the iShop Item has no image.
- Run `bench build --app logicx_ishop` on each site. This release changes only the Item client script.

## v-1.0.8

### [v 1.0.8] 2026-08-14 6:11 pm - Item iShop tab after the UOM table

#### Database Changes

- Database update: Yes (auto-check).
- FIXED: Moved the `ishop_tab` Tab Break on ERPNext Item from after `details` to after `uoms`, so the iShop
  tab now follows the Units of Measure table. The `ishop_item_details_html` field stays anchored to
  `ishop_tab` and moves with it.
- Added the post-model-sync patch `logicx_ishop.patches.move_item_ishop_tab_after_uoms`, which
  rewrites the Custom Field position on sites that already applied
  `logicx_ishop.patches.add_item_ishop_tab` and clears the Item cache. The patch is safe to rerun.
- Run `bench --site <site> migrate` on each site.

#### App Codebase Changes

- Bumped the LogicX iShop version to 1.0.8.
- Changed the `insert_after` value of the Item iShop tab Custom Field definition to `uoms`.
- Added tests for the new tab position and for the move from the previous `details` position.

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

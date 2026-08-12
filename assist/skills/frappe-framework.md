# Frappe Framework Reference

## Purpose

This file routes developers and agents to the correct Frappe guidance.

The official Frappe documentation remains the source for framework behavior.

## Application structure

Use a Frappe app as a Python package inside a Bench `apps` directory.

Keep active application metadata in `hooks.py`, `modules.txt`, `patches.txt`, and `pyproject.toml`.

Official sources:

- [Frappe Apps](https://docs.frappe.io/framework/user/en/basics/apps)
- [Create an App](https://docs.frappe.io/framework/user/en/tutorial/create-an-app)
- [Bench Directory Structure](https://docs.frappe.io/framework/user/en/basics/directory-structure)

## DocTypes and controllers

DocType JSON defines the model and standard form metadata.

A controller extends `frappe.model.document.Document` and owns document lifecycle behavior.

Use `validate` to reject invalid document state before a save.

Official sources:

- [Frappe Framework Basics](https://docs.frappe.io/framework/user/en/basics)
- [DocType Controllers](https://docs.frappe.io/framework/user/en/basics/doctypes/controllers)

## Permissions

Define the default role permissions in each DocType.

Check permissions again in custom queries and remote actions.

Use permission levels only for fields that need a separate access level.

Official sources:

- [Users and Permissions](https://docs.frappe.io/framework/user/en/basics/users-and-permissions)
- [Permission Types](https://docs.frappe.io/framework/permission-types)

## Hooks

Use hooks to extend framework behavior with a clear application owner.

Prefer `extend_doctype_class` for standard DocType extensions on Frappe v16 and later.

Official source:

- [Frappe Hooks](https://docs.frappe.io/framework/user/en/python-api/hooks)

## Database access

Prefer document APIs when validation and lifecycle hooks must run.

Use `frappe.db.set_value` only when bypassing ORM hooks is intentional.

Do not call manual commits in normal request code.

Official source:

- [Frappe Database API](https://docs.frappe.io/framework/user/en/api/database)

## REST and whitelisted methods

Frappe exposes DocTypes through resource endpoints.

Whitelisted Python methods are available through method endpoints.

Use `POST` when a remote method changes database state.

Official source:

- [Frappe REST API](https://docs.frappe.io/framework/user/en/api/rest)

## Migrations

Run a site migration after schema, patch, fixture, hook, or scheduler changes.

Add data patches to `patches.txt` in execution order.

Do not edit a released patch after sites can apply it.

Official source:

- [Database Migrations](https://docs.frappe.io/framework/user/en/database-migrations)

## Background jobs

Use `frappe.enqueue` for work that should not block a request.

Use `enqueue_after_commit=True` when a job reads data written by the request.

Run a migration after scheduler event changes.

Official source:

- [Background Jobs](https://docs.frappe.io/framework/user/en/api/background_jobs)

## Tests

Use `FrappeTestCase` for tests that need Frappe site and database behavior.

Run focused tests before the full application suite.

```bash
bench --site <site> run-tests --doctype "iShop Item"
bench --site <site> run-tests --module logicx_ishop.logicx_ishop.doctype.ishop_item.test_ishop_item
bench --site <site> run-tests --app logicx_ishop
```

Official sources:

- [Frappe Testing](https://docs.frappe.io/framework/user/en/testing)
- [Frappe Unit Testing](https://docs.frappe.io/framework/user/en/guides/automated-testing/unit-testing)

## Bench commands

Run site commands from the Bench root and pass an explicit site.

Official source:

- [Bench Commands Cheatsheet](https://docs.frappe.io/framework/user/en/bench/resources/bench-commands-cheatsheet)

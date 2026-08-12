### LogicX iShop

LogicX online shopping experience.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch version-16
bench install-app logicx_ishop
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/logicx_ishop
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### Release commands

The Python package version is the source for all release commands.

```bash
python tools/version.py show
python tools/version.py check
python tools/version.py bump --title "Version update"
python tools/github_now.py --dry-run
```

Use the same workflow from an installed Bench app:

```bash
bench --site <site> logicx-ishop-release show
bench --site <site> logicx-ishop-release check
bench --site <site> logicx-ishop-release bump --title "Version update"
bench --site <site> logicx-ishop-release github-now --dry-run
```

The GitHub workflow asks before it pulls, stages, commits, or pushes changes.

### License

mit

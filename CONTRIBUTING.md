# Contributing to Budgie

Thanks for taking the time to help. This guide covers setup, the project rules, and what a pull request needs before review.

## Getting set up

Follow the [installation guide](docs/getting-started/installation.md), then read the [architecture overview](docs/architecture/overview.md) and the [code guide](docs/development/code-guide.md). They explain where things live and which mixins to reuse.

## Reporting bugs and ideas

Open an [issue](https://github.com/rheinitz/Budgie/issues) and include:

- what you did, what you expected, and what happened;
- the page URL, and a screenshot if it is visual;
- your OS and Python version for setup problems.

## Project rules

These keep the project within its scope. Please discuss before breaking one.

- **The database stays empty.** No fixtures, data migrations or seed scripts. Everything is created through the UI.
- **No custom JavaScript.** Only the Bootstrap bundle. Interactions use links and forms.
- **No new packages** beyond those in `requirements.txt` without agreement in an issue first.
- **No authentication.** Budgie has no login, logout or registration.
- **Never commit** `.env`, `db.sqlite3`, the virtual environment or local notes.

## Branches

Branch from `main` and name the branch after the kind of change:

| Prefix | Use for |
| --- | --- |
| `feat/` | New behavior, for example `feat/month-summary` |
| `fix/` | Bug fixes |
| `refactor/` | Code changes that keep behavior, for example `refactor/types-and-transactions` |
| `style/` | CSS and visual changes |
| `docs/` | Documentation only |
| `chore/` | Settings, dependencies, tooling |

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/) with the same prefixes: `feat:`, `fix:`, `refactor:`, `style:`, `docs:`, `chore:`.

```text
feat: filter, sort and paginate transactions
fix: keep filters when changing page
docs: add architecture overview
```

Keep each commit to one logical change. Stage explicit paths and check `git status` before committing.

## Code style

The [code guide](docs/development/code-guide.md#conventions) lists the conventions. In short: PEP 8, type hints everywhere, class-based views, explicit form `fields`, `Decimal` from strings, and `{% url %}` instead of hard-coded paths.

## Before you open a pull request

Run these from the project root with the virtual environment active:

```bash
python manage.py check                              # System check identified no issues
python manage.py makemigrations --check --dry-run   # No changes detected
python manage.py test                               # runs any tests you added
```

Then check by hand:

1. Every page you touched is reachable through links and shows the navbar and footer.
2. Forms show Django's error messages for bad input, not just browser warnings.
3. The page works in both light and dark themes and on a narrow screen.
4. After deleting `db.sqlite3` and running `migrate`, the empty states make sense.
5. If the change is visible, update the screenshots in [`docs/screenshots/`](docs/screenshots/) and the docs that mention it.

## Pull requests

- Target `main` and keep the PR focused on one change.
- Describe what changed and why, and how you tested it.
- Add screenshots for visual changes.
- Link the issue it closes, for example `Closes #12`.

## Contributors

Budgie is maintained by [@rheinitz](https://github.com/rheinitz). Everyone who has contributed is listed on the [contributors page](https://github.com/rheinitz/Budgie/graphs/contributors).

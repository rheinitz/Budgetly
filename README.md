<h1><img src="static/images/favicon.png" alt="" width="48"> BUDGIE</h1>

<p>
  <img src="https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/django-6.1-092E20?logo=django&logoColor=white" alt="Django 6.1">
  <img src="https://img.shields.io/badge/bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white" alt="Bootstrap 5.3">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT license"></a>
</p>

## Introduction

Budgie tracks a budget one month at a time. Every amount belongs to one of four categories — Income, Expenses, Savings or Investments — and the month page turns them into totals, a net figure and a savings rate.

![Budgie demo](docs/screenshots/demo.gif)

## How It Works

Create **types** such as Salary, Groceries or ETF, each inside one of four fixed **categories**: Income, Expenses, Savings and Investments. Log **transactions** against them, optionally with **tags** like `summer-trip`. Each month page then shows the totals, the net amount and your savings rate.

- Monthly totals, net and savings rate, with previous and next month navigation
- Tags that group spending across categories and months
- Search, filters, sorting and pagination over all transactions
- Server-side validation with clear messages, and protected deletes
- Light and dark themes with no custom JavaScript

| Month page | All transactions | Light theme |
| --- | --- | --- |
| ![Month page](docs/screenshots/month.png) | ![All transactions](docs/screenshots/transactions.png) | ![Light theme](docs/screenshots/month-light.png) |

## Quick Start

```bash
git clone https://github.com/rheinitz/budgie.git && cd budgie
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. The app needs no `.env` file and starts with an empty database. See the [installation guide](docs/getting-started/installation.md) for Windows, environment variables and the 404 page, and the [user guide](docs/getting-started/user-guide.md) for a first walk through.

## Documentation

| | |
| --- | --- |
| [Getting Started](docs/getting-started/installation.md) | Installation, configuration and the [User Guide](docs/getting-started/user-guide.md) |
| [Architecture](docs/architecture/overview.md) | Apps, the [Data Model](docs/architecture/data-model.md), and [URLs, Views and Templates](docs/architecture/urls-and-views.md) |
| [Development](docs/development/code-guide.md) | Code conventions and where to add a feature |
| [All docs](docs/README.md) | The full index and every screenshot |

## Contributing

Issues and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the branch and commit conventions and the checks to run first.

## License

[MIT](LICENSE) © 2026 rheinitz

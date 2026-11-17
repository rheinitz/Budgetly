# Exam requirements

[Docs home](../README.md) · Previous: [Code guide](code-guide.md)

Budgie is the project for the SoftUni Django Basics retake exam. This table maps each requirement to where it is met.

| Requirement | Where it is met |
| --- | --- |
| At least 3 apps, one responsibility each | `common`, `categories`, `tags`, `transactions`. See [Architecture overview](../architecture/overview.md#apps). |
| At least 3 models, with many-to-one and many-to-many relations | `Type`, `Tag`, `Transaction`. Transaction to Type is a foreign key; Transaction to Tag is many-to-many. See [Data model](../architecture/data-model.md). |
| At least 4 forms | `TypeForm`, `TagForm`, `TransactionForm`, `TransactionFilterForm`, plus three delete forms |
| Validation in models and forms | Field validators, `Type.clean()`, `validate_not_in_future`, `TagForm.clean_name()`, `TransactionFilterForm.clean()` |
| Labels, placeholders, help texts, custom error messages | Every form's `Meta` |
| At least one disabled field | All delete forms; `Type.category` on edit once the type has transactions |
| Confirmation before every delete | Three confirm-delete pages |
| GET / POST handling, redirect after success, friendly errors | All create, edit and delete views. See [View behavior](../architecture/urls-and-views.md#view-behavior-worth-knowing). |
| At least 12 templates, at least 8 dynamic | 16 page templates, 14 dynamic. See [Templates](../architecture/urls-and-views.md#templates). |
| Full CRUD | Type, Tag and Transaction |
| Lists, filtered and sorted lists, detail pages | Type and tag lists, the month page, all transactions with filters, sorting and pagination, three detail pages |
| Built-in template filters and tags | `date`, `truncatechars`, `default`, `capfirst`, `join`, `pluralize`, `urlencode`, `widthratio`, `querystring`, `now`, `url`, `include`, `with`, `static` |
| Custom filter and tag | `money` filter and `totals_cards` inclusion tag in `common/templatetags/budgie_tags.py` |
| Custom 404 page, base layout, partials, navbar and footer, no orphan pages | `404.html`, `base.html`, `templates/partials/` |
| Bootstrap design | Bootstrap 5.3 from the CDN plus `static/css/`, with light and dark themes |
| Runs on an empty database with default settings; environment variables documented | Defaults in `config/settings.py`, `.env.example`, [Installation](../getting-started/installation.md#2-environment-variables-optional) |

## Beyond the requirements

- A chainable custom QuerySet attached with `.as_manager()`.
- Grouped aggregation with `values().annotate(Sum)` in one query, and `annotate(Count)` for list counts.
- `select_related` and `prefetch_related` to keep the query count flat.
- `{% querystring %}` pagination that keeps filters.
- `RestrictedError` handling on delete.
- Input normalization for tag names.
- A theme switch built from a view, a cookie and a context processor, with no custom JavaScript.

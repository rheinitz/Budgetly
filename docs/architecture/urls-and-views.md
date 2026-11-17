# URLs, views and templates

[Docs home](../README.md) · Previous: [Data model](data-model.md) · Next: [Code guide](../development/code-guide.md)

Every link is reversed by name, for example `{% url 'types:detail' type.pk %}` or `get_absolute_url()`. No internal URL is hard-coded.

## Routes

| Path | Name | View | Template |
| --- | --- | --- | --- |
| `/` | `common:home` | `HomeView` | `common/home.html` |
| `/about/` | `common:about` | `AboutView` | `common/about.html` |
| `/theme/<theme>/` | `common:theme` | `set_theme` (function) | redirect |
| `/types/` | `types:list` | `TypeListView` | `categories/type_list.html` |
| `/types/add/` | `types:add` | `TypeCreateView` | `categories/type_form.html` |
| `/types/<pk>/` | `types:detail` | `TypeDetailView` | `categories/type_detail.html` |
| `/types/<pk>/edit/` | `types:edit` | `TypeUpdateView` | `categories/type_form.html` |
| `/types/<pk>/delete/` | `types:delete` | `TypeDeleteView` | `categories/type_confirm_delete.html` |
| `/tags/` | `tags:list` | `TagListView` | `tags/tag_list.html` |
| `/tags/add/` | `tags:add` | `TagCreateView` | `tags/tag_form.html` |
| `/tags/<pk>/` | `tags:detail` | `TagDetailView` | `tags/tag_detail.html` |
| `/tags/<pk>/edit/` | `tags:edit` | `TagUpdateView` | `tags/tag_form.html` |
| `/tags/<pk>/delete/` | `tags:delete` | `TagDeleteView` | `tags/tag_confirm_delete.html` |
| `/transactions/` | `transactions:list` | `TransactionListView` | `transactions/transaction_list.html` |
| `/transactions/current/` | `transactions:current` | `current_month` (function) | redirect |
| `/transactions/<year>/<month>/` | `transactions:month` | `MonthTransactionsView` | `transactions/transaction_month.html` |
| `/transactions/add/` | `transactions:add` | `TransactionCreateView` | `transactions/transaction_form.html` |
| `/transactions/<pk>/` | `transactions:detail` | `TransactionDetailView` | `transactions/transaction_detail.html` |
| `/transactions/<pk>/edit/` | `transactions:edit` | `TransactionUpdateView` | `transactions/transaction_form.html` |
| `/transactions/<pk>/delete/` | `transactions:delete` | `TransactionDeleteView` | `transactions/transaction_confirm_delete.html` |
| `/admin/` | `admin:index` | Django admin | optional, never needed |

The `categories` app is mounted at `/types/` with the URL namespace `types`, because the pages manage types. The four categories themselves have no pages.

## View behavior worth knowing

- **Redirect after success.** Types and tags redirect to their detail page through `get_absolute_url()`. Transactions redirect to the month they belong to through `TransactionMonthRedirectMixin`, so the new row and the updated totals are visible right away.
- **Delete confirmations reuse the model forms** with every field disabled (`DisabledFieldsMixin`). `DeleteFormInstanceMixin` passes `instance=self.object` to the form, so the fields show the record and uniqueness checks do not report it as its own duplicate.
- **`TypeDeleteView`** hides the delete button when the type has transactions and catches `RestrictedError` as a safety net if one is added in another tab.
- **`TypeCreateView`** pre-selects the category from `?category=expense`, which the "Add to ..." links on the types page use.
- **`TransactionListView`** binds `TransactionFilterForm` to the query string. A valid form chains `search().in_category().with_tag().between()` and sorts with `-pk` as a tie-breaker so pages never repeat rows. An invalid form, such as a start date after the end date, shows the error above the unfiltered list.
- **`current_month`** redirects to today's month, so "This month" links never go stale.
- **`set_theme`** accepts only `dark` or `light` (anything else is a 404), stores a one-year `theme` cookie, and redirects to `?next=` only if it points back to this site.

## Templates

```text
templates/
├── base.html          layout, fonts, CSS links, navbar and footer
├── 404.html
├── partials/          navbar, footer, form_fields, empty_state, transactions_table,
│                      tag_badges, totals_cards, month_nav, pagination
├── common/            home, about
├── categories/        type_list, type_detail, type_form, type_confirm_delete
├── tags/              tag_list, tag_detail, tag_form, tag_confirm_delete
└── transactions/      transaction_list, transaction_month, transaction_detail,
                       transaction_form, transaction_confirm_delete
```

That is 16 page templates, 14 of them dynamic, plus the base layout and nine partials. Every page extends `base.html`, so the navbar and footer appear everywhere, and every page is reachable through links.

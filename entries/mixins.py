class EntryMonthRedirectMixin:
    def get_success_url(self) -> str:
        return self.object.get_month_url()

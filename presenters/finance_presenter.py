class FinancePresenter:
    def __init__(self, view, repository):
        self.view = view
        self.repository = repository

    def refresh(self):
        records = self.repository.fetch_all()
        self.view.show_records(records)

    def open_add(self):
        self.view.open_add_dialog()

    def open_edit(self):
        record = self.view.get_selected()
        if not record:
            return
        self.view.open_edit_dialog(record)

    # ===== CRUD =====

    def add_record(self, description, costs, total):
        self.repository.add(description, costs, total)
        self.refresh()

    def edit_record(self, record_id, description, costs, total):
        self.repository.update(record_id, description, costs, total)
        self.refresh()

    def delete_record(self):
        ids = self.view.get_selected_ids()
        for record_id in ids:
            self.repository.delete(record_id)
        self.refresh()

import tkinter as tk
from tkinter import ttk
from toolbar import Toolbar
from dialogs import AddDialog, EditDialog


class Main(tk.Frame):
    def __init__(self, root, db):
        super().__init__(root)
        self.db = db
        self._init_ui()
        self.refresh()

    def _init_ui(self):
        self.toolbar = Toolbar(self, {
            'add': self.open_add,
            'edit': self.open_edit,
            'delete': self.delete_record,
            'refresh': self.refresh
        })
        self.toolbar.pack(fill=tk.X)

        self.tree = ttk.Treeview(
            self,
            columns=('id', 'description', 'costs', 'total'),
            show='headings'
        )

        for col, text, width in [
            ('id', 'ID', 30),
            ('description', 'Наименование', 300),
            ('costs', 'Статья', 150),
            ('total', 'Сумма', 100)
        ]:
            self.tree.heading(col, text=text)
            self.tree.column(col, width=width, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        for row in self.db.fetch_all():
            self.tree.insert('', tk.END, values=row)

    def open_add(self):
        AddDialog(self, self.add_record, "Добавить!")

    def open_edit(self):
        selected = self.tree.selection()
        if not selected:
            return
        record = self.tree.item(selected[0])['values']
        EditDialog(self, record, self.edit_record, "Применить!")

    def add_record(self, description, costs, total):
        self.db.add(description, costs, total)
        self.refresh()

    def edit_record(self, record_id, description, costs, total):
        self.db.update(record_id, description, costs, total)
        self.refresh()

    def delete_record(self):
        for item in self.tree.selection():
            record_id = self.tree.item(item)['values'][0]
            self.db.delete(record_id)
        self.refresh()

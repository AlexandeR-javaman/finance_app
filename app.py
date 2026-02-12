import tkinter as tk
from tkinter import ttk
from views.toolbar import Toolbar
from views.dialogs import AddDialog, EditDialog


class App(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.presenter = None
        self._init_ui()

    def set_presenter(self, presenter):
        self.presenter = presenter

    def _init_ui(self):
        self.toolbar = Toolbar(self, {
            'add': lambda: self.presenter.open_add(),
            'edit': lambda: self.presenter.open_edit(),
            'delete': lambda: self.presenter.delete_record(),
            'refresh': lambda: self.presenter.refresh()
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
# ===== Методы отображения =====

    def show_records(self, records):
        self.tree.delete(*self.tree.get_children())
        for row in records:
            self.tree.insert('', tk.END, values=row)

    def get_selected(self):
        selected = self.tree.selection()
        if not selected:
            return None
        return self.tree.item(selected[0])['values']

    def get_selected_ids(self):
        ids = []
        for item in self.tree.selection():
            ids.append(self.tree.item(item)['values'][0])
        return ids

    def open_add_dialog(self):
        AddDialog(self, self.presenter.add_record, "Добавить!")

    def open_edit_dialog(self, record):
        EditDialog(self, record, self.presenter.edit_record, "Применить!")
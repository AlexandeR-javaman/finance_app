from tkinter import messagebox
from .base_dialog import BaseDialog

class AddDialog(BaseDialog):
    def __init__(self, parent, on_submit, text_apply_button):
        super().__init__(parent, 'Добавить позицию', text_apply_button, on_submit)

    def submit(self):
        name = self.desc.get().strip()
        total_text = self.total.get()

        if not name:
            messagebox.showerror("Ошибка", "Наименование не может быть пустым")
            return

        if total_text == "":
            messagebox.showerror("Ошибка", "Сумма не может быть пустой")
            return
        self.on_submit(
            name,
            self.costs.get(),
            float(total_text)
        )
        self.destroy()

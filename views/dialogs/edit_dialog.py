from tkinter import messagebox
from .base_dialog import BaseDialog

class EditDialog(BaseDialog):
    def __init__(self, parent, record, on_submit, text_apply_button):
        super().__init__(parent, 'Редактировать позицию', text_apply_button, on_submit)
        
        self.record_id = record[0]
        self.desc.insert(0, record[1])
        self.costs.set(record[2])
        self.total.insert(0, record[3])

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
            self.record_id,
            name,
            self.costs.get(),
            float(total_text)
        )
        self.destroy()
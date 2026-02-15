import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class BaseDialog(tk.Toplevel):
    def __init__(self, parent, title, text_apply_button, on_submit):
        super().__init__(parent)
        self.on_submit = on_submit
        self.title(title)
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        self._init_ui(text_apply_button)
        self.grab_set()
        self.focus_set()
    
    def _init_ui(self, text_apply_button):
        ttk.Label(self, text='Наименование').place(x=50, y=50)
        ttk.Label(self, text='Статья').place(x=50, y=80)
        ttk.Label(self, text='Сумма').place(x=50, y=110)

        self.desc = ttk.Entry(self)
        self.costs = ttk.Combobox(self, values=['Доход', 'Расход'])
        self.total = ttk.Entry(self, validate="key")

        # Валидация: только цифры и точка
        vcmd = (self.register(self._validate_number), "%P")
        self.total.config(validatecommand=vcmd)

        self.costs.current(0)

        self.desc.place(x=200, y=50)
        self.costs.place(x=200, y=80)
        self.total.place(x=200, y=110)

        ttk.Button(self, text=text_apply_button, command=self.submit).place(x=220, y=170)
    
    def _validate_number(self, P):
        """Разрешаем ввод только цифр и точки"""
        if P == "":
            return True
        try:
            float(P)
            return True
        except ValueError:
            return False

    def submit(self):
        pass
import tkinter as tk
from tkinter import ttk


class BaseDialog(tk.Toplevel):
    def __init__(self, parent, title, text_apply_button):
        super().__init__(parent)
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
        self.total = ttk.Entry(self)

        self.costs.current(0)

        self.desc.place(x=200, y=50)
        self.costs.place(x=200, y=80)
        self.total.place(x=200, y=110)

        ttk.Button(self, text=text_apply_button, command=self.submit).place(x=220, y=170)
    
    def submit(self):
        pass



class AddDialog(BaseDialog):
    def __init__(self, parent, on_submit, text_apply_button):
        super().__init__(parent, 'Добавить позицию', text_apply_button)
        self.on_submit = on_submit

    def submit(self):
        self.on_submit(
            self.desc.get(),
            self.costs.get(),
            self.total.get()
        )
        self.destroy()


class EditDialog(BaseDialog):
    def __init__(self, parent, record, on_submit, text_apply_button):
        super().__init__(parent, 'Редактировать позицию', text_apply_button)
        self.on_submit = on_submit
        
        self.record_id = record[0]
        self.desc.insert(0, record[1])
        self.costs.set(record[2])
        self.total.insert(0, record[3])

    def submit(self):
        self.on_submit(
            self.record_id,
            self.desc.get(),
            self.costs.get(),
            self.total.get()
        )
        self.destroy()


# import tkinter as tk
# from tkinter import ttk


# class BaseDialog(tk.Toplevel):
#     def __init__(self, parent, title):
#         super().__init__(parent)
#         self.title(title)
#         self.geometry('400x220+400+300')
#         self.resizable(False, False)
#         self.grab_set()
#         self.focus_set()


# class AddDialog(BaseDialog):
#     def __init__(self, parent, on_submit, text_apply_button):
#         super().__init__(parent, 'Добавить позицию')
#         self.on_submit = on_submit
#         # self.text_apply_button = text_apply_button
#         self._init_ui(text_apply_button)

#     def _init_ui(self, text_apply_button):
#         ttk.Label(self, text='Наименование').place(x=50, y=50)
#         ttk.Label(self, text='Статья').place(x=50, y=80)
#         ttk.Label(self, text='Сумма').place(x=50, y=110)

#         self.desc = ttk.Entry(self)
#         self.costs = ttk.Combobox(self, values=['Доход', 'Расход'])
#         self.total = ttk.Entry(self)

#         self.costs.current(0)

#         self.desc.place(x=200, y=50)
#         self.costs.place(x=200, y=80)
#         self.total.place(x=200, y=110)

#         ttk.Button(self, text=text_apply_button, command=self.submit).place(x=220, y=170)

#     def submit(self):
#         self.on_submit(
#             self.desc.get(),
#             self.costs.get(),
#             self.total.get()
#         )
#         self.destroy()


# class EditDialog(AddDialog):
#     def __init__(self, parent, record, on_submit, text_apply_button):
#         self.record_id = record[0]
#         # self.text_apply_button = text_apply_button
#         super().__init__(parent, on_submit, text_apply_button)
#         self.title('Редактировать')

#         self.desc.insert(0, record[1])
#         self.costs.set(record[2])
#         self.total.insert(0, record[3])

#     def submit(self):
#         self.on_submit(
#             self.record_id,
#             self.desc.get(),
#             self.costs.get(),
#             self.total.get()
#         )
#         self.destroy()

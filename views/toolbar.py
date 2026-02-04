from pathlib import Path
import tkinter as tk


class Toolbar(tk.Frame):
    def __init__(self, parent, callbacks):
        super().__init__(parent, bg='#d7d8e0', bd=2)
        self.callbacks = callbacks
        self._init_ui()
    
    def _init_ui(self):
        buttons = [
            ('add.png', 'Добавить', self.callbacks['add']),
            ('update.png', 'Редактировать', self.callbacks['edit']),
            ('delete.png', 'Удалить', self.callbacks['delete']),
            ('refresh.png', 'Обновить', self.callbacks['refresh']),
        ]

        # путь к картинкам динамический относительно текущей папки
        # Получаем путь к текущей директории (где лежит скрипт)
        current_dir = Path(__file__).parent  # ..\VS Code\finance_app\views

        # Поднимаемся на уровень выше (в finance_app)
        parent_dir = current_dir.parent  # ..\VS Code\finance_app

        # Формируем путь к нужной папке
        img_dir = parent_dir / "resources" / "icons"

        self.images = []
        self.buttons = {} # для создания словаря кнопок, чтобы потом можно было изменить цвет или заблокировать отдельные кнопки
        for img_file, text, cmd in buttons:
            img_path = img_dir / img_file
            image = tk.PhotoImage(file=str(img_path))
            self.images.append(image)
            btn = tk.Button(
            # tk.Button( #если не надо помещать кнопки в словарь, то можно объявлять их без присваивания переменной
                self,
                text=text,
                image=image,
                compound=tk.TOP,
                bg='#d7d8e0',
                bd=0,
                command=cmd
            ).pack(side=tk.LEFT, padx=2, pady=2)
            self.buttons[text] = btn  # ключ — текст кнопки

# import tkinter as tk
# from pathlib import Path

# class Toolbar(tk.Frame):
#     def __init__(self, parent, callbacks: dict):
#         """
#         callbacks: словарь с ключами 'add', 'edit', 'delete', 'refresh' и функциями для них
#         """
#         super().__init__(parent, bg='#d7d8e0', bd=2)
#         self._images = []  # храним ссылки на картинки, чтобы tkinter их не удалил
#         self._callbacks = callbacks
#         self._init_ui()

#     def _init_ui(self):
#         # путь к картинкам можно сделать динамическим, например относительно текущей папки
#         img_dir = Path(__file__).parent

#         buttons = [
#             ('add.png', 'Добавить', 'add'),
#             ('update.png', 'Редактировать', 'edit'),
#             ('delete.png', 'Удалить', 'delete'),
#             ('refresh.png', 'Обновить', 'refresh'),
#         ]

#         for img_file, text, key in buttons:
#             img_path = img_dir / img_file
#             image = tk.PhotoImage(file=str(img_path))
#             self._images.append(image)  # сохраняем ссылку
#             btn = tk.Button(
#                 self,
#                 text=text,
#                 image=image,
#                 compound=tk.TOP,
#                 bg='#d7d8e0',
#                 bd=0,
#                 command=self._callbacks[key]
#             )
#             btn.pack(side=tk.LEFT, padx=2, pady=2)


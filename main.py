import sys
sys.dont_write_bytecode = True

import tkinter as tk
from app import App
from utils.db import FinanceDB


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Household finance')
    root.geometry('650x450+300+200')
    root.resizable(False, False)

    db = FinanceDB()
    app = App(root, db)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

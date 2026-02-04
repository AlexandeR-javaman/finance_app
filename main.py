import sys
sys.dont_write_bytecode = True

import tkinter as tk
from app import Main
from utils.db import FinanceDB


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Household finance')
    root.geometry('650x450+300+200')
    root.resizable(False, False)

    db = FinanceDB()
    app = Main(root, db)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

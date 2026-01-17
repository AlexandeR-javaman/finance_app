import tkinter as tk
from main import Main
from db import FinanceDB


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Household finance')
    root.geometry('650x450+300+200')
    root.resizable(False, False)

    db = FinanceDB()
    app = Main(root, db)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

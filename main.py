import sys
sys.dont_write_bytecode = True

import tkinter as tk
from app import App
from repositories.sqlite_finance_repository import SQLiteFinanceRepository
from presenters.finance_presenter import FinancePresenter


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Household finance')
    root.geometry('650x450+300+200')
    root.resizable(False, False)

    repository = SQLiteFinanceRepository()

    view = App(root)
    presenter = FinancePresenter(view, repository)

    view.set_presenter(presenter)
    presenter.refresh()

    view.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

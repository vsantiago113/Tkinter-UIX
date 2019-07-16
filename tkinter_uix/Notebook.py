from tkinter.ttk import Notebook as NB
from tkinter import ttk


class Notebook(ttk.Notebook):
    def __init__(self, master, **kwargs):
        ttk.Notebook.__init__(self, master, **kwargs)

        s = ttk.Style()
        s.configure('TNotebook.Tab', font=('Verdana', '12'), padding=(14, 6), foreground='#212121')
        s.configure('TNotebook', background='#fafafa')
        s.map('TNotebook.Tab', foreground=[('selected', '#4285F4')])


if __name__ == '__main__':
    pass

from tkinter import Label as _Label


class Label(_Label):
    def __init__(self, master, *args, **kwargs):
        _Label.__init__(self, master, font=('Verdana', 12), bg='#fafafa', fg='#212121', *args, **kwargs)


if __name__ == '__main__':
    pass

import tkinter


class BTNPrimary(tkinter.Label):
    def __init__(self, master, command=None, *args, **kwargs):
        tkinter.Label.__init__(self, master, *args, **kwargs)

        # To add a border: (relief=tkinter.SOLID, borderwidth=2)
        self.configure(bd=0, padx=16, pady=8, bg='#4285F4', fg='#fafafa', relief=tkinter.FLAT)

        self.bind('<Enter>', self.label_on_hover)
        self.bind('<Leave>', self.label_off_hover)
        self.bind('<Button-1>', lambda event: self.on_click(command))

    def label_on_hover(self, *args):
        self.configure(bg='#0d47a1', cursor="hand2")

    def label_off_hover(self, *args):
        self.configure(bg='#4285F4', fg='#fafafa')

    def on_click(self, command):
        self.configure(fg='#2E2E2E')
        if command:
            command()


class BTNInfo(tkinter.Label):
    def __init__(self, master, command=None, *args, **kwargs):
        tkinter.Label.__init__(self, master, *args, **kwargs)

        # To add a border: (relief=tkinter.SOLID, borderwidth=2)
        self.configure(bd=0, padx=16, pady=8, bg='#33b5e5', fg='#fafafa', relief=tkinter.FLAT)

        self.bind('<Enter>', self.label_on_hover)
        self.bind('<Leave>', self.label_off_hover)
        self.bind('<Button-1>', lambda event: self.on_click(command))

    def label_on_hover(self, *args):
        self.configure(bg='#0099CC', cursor="hand2")

    def label_off_hover(self, *args):
        self.configure(bg='#33b5e5', fg='#fafafa')

    def on_click(self, command):
        self.configure(fg='#2E2E2E')
        if command:
            command()


class BTNSuccess(tkinter.Label):
    def __init__(self, master, command=None, *args, **kwargs):
        tkinter.Label.__init__(self, master, *args, **kwargs)

        # To add a border: (relief=tkinter.SOLID, borderwidth=2)
        self.configure(bd=0, padx=16, pady=8, bg='#00C851', fg='#fafafa', relief=tkinter.FLAT)

        self.bind('<Enter>', self.label_on_hover)
        self.bind('<Leave>', self.label_off_hover)
        self.bind('<Button-1>', lambda event: self.on_click(command))

    def label_on_hover(self, *args):
        self.configure(bg='#007E33', cursor="hand2")

    def label_off_hover(self, *args):
        self.configure(bg='#00C851', fg='#fafafa')

    def on_click(self, command):
        self.configure(fg='#2E2E2E')
        if command:
            command()


class BTNDanger(tkinter.Label):
    def __init__(self, master, command=None, *args, **kwargs):
        tkinter.Label.__init__(self, master, *args, **kwargs)

        # To add a border: (relief=tkinter.SOLID, borderwidth=2)
        self.configure(bd=0, padx=16, pady=8, bg='#ff4444', fg='#fafafa', relief=tkinter.FLAT)

        self.bind('<Enter>', self.label_on_hover)
        self.bind('<Leave>', self.label_off_hover)
        self.bind('<Button-1>', lambda event: self.on_click(command))

    def label_on_hover(self, *args):
        self.configure(bg='#CC0000', cursor="hand2")

    def label_off_hover(self, *args):
        self.configure(bg='#ff4444', fg='#fafafa')

    def on_click(self, command):
        self.configure(fg='#2E2E2E')
        if command:
            command()


class BTNWarning(tkinter.Label):
    def __init__(self, master, command=None, *args, **kwargs):
        tkinter.Label.__init__(self, master, *args, **kwargs)

        # To add a border: (relief=tkinter.SOLID, borderwidth=2)
        self.configure(bd=0, padx=16, pady=8, bg='#ffbb33', fg='#2E2E2E', relief=tkinter.FLAT)

        self.bind('<Enter>', self.label_on_hover)
        self.bind('<Leave>', self.label_off_hover)
        self.bind('<Button-1>', lambda event: self.on_click(command))

    def label_on_hover(self, *args):
        self.configure(bg='#FF8800', cursor="hand2")

    def label_off_hover(self, *args):
        self.configure(bg='#ffbb33', fg='#2E2E2E')

    def on_click(self, command):
        self.configure(fg='#fafafa')
        if command:
            command()


if __name__ == '__main__':
    pass

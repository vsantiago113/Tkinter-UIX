import tkinter
from PIL import Image, ImageTk


class Navbar(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)

        default_image = Image.open('./images/python.png')
        self.image = ImageTk.PhotoImage(default_image)
        self.header_title = tkinter.Label(self, image=self.image, text='Title', compound=tkinter.LEFT)
        self.header_title.pack(side=tkinter.LEFT)

        self.show()

    def show(self):
        self.pack(side=tkinter.TOP, fill=tkinter.X)

    def hide(self):
        self.pack_forget()

    @staticmethod
    def add_widget(widget):
        widget.pack(side=tkinter.RIGHT, padx=3, pady=3)

    def edit(self, **kwargs):
        self.header_title.configure(**kwargs)


if __name__ == '__main__':
    pass

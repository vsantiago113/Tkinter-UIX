import tkinter
from tkinter import messagebox
from tkinter_uix.Layout import AnchorLayout, BoxLayout
from tkinter_uix.Screen import ScreenManager
from tkinter_uix.Button import Button
from tkinter_uix.Label import Label
from tkinter_uix.Navbar import Navbar
from tkinter_uix.Entry import Entry

# App Global Username and Password
username_key = str()
password_key = str()


class MainWin:
    def __init__(self, parent, screen_manager):
        self.screen_manager = screen_manager

        user_screen = self.screen_manager.add_screen(parent, 'user_screen')
        self.screen_manager.switch_screen('user_screen')

        # START Navigation Bar **
        self.navbar = Navbar(user_screen)

        home_button = Button(self.navbar, text='Home', color='info', command=None)
        logout_button = Button(self.navbar, text='Logout', color='info',
                               command=lambda: self.screen_manager.switch_screen('login_screen'))

        self.navbar.add_widget(logout_button)
        self.navbar.add_widget(home_button)
        # END Navigation Bar **

        def testme():
            print(button.text)

        def testme2(string):
            button.text = string

        boxlayout = BoxLayout(user_screen)
        button = Button(boxlayout, text='Get this text', command=testme)
        button.pack()

        button2 = Button(boxlayout, text='Change me', command=lambda: testme2('Hello'))
        button2.pack()


def my_app():
    root = tkinter.Tk()
    root.geometry('700x500')

    def login(*args):
        global username_key, password_key
        username_key = username.get()
        password_key = password.get()

        if username.get() == 'admin' and password.get() == 'Admin123':
            password.delete(0, tkinter.END)
            MainWin(root, screen_manager)
        else:
            messagebox.showerror('Login Failed!', 'Incorrect username or password!')

    screen_manager = ScreenManager()
    login_screen = screen_manager.add_screen(root, 'login_screen')
    screen_manager.switch_screen('login_screen')

    anchor = AnchorLayout(login_screen, anchor='CENTER')

    username_label = Label(anchor, text='Username')
    username_label.pack()
    username = Entry(anchor, placeholder='Username...', on_return=login)
    username.pack(pady=(0, 10))

    password_label = Label(anchor, text='Password')
    password_label.pack()
    password = Entry(anchor, show='*', placeholder='Password...', on_return=login)
    password.pack(pady=(0, 10))

    button = Button(anchor, text='Login', command=login)
    button.pack()

    root.mainloop()


if __name__ == '__main__':
    my_app()

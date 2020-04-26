from tkinter import Label as BTN
from tkinter import FLAT
from typing import NoReturn


class Button(BTN):
    def __init__(self, master, text='', command=None, color='default', disabled=False, *args, **kwargs):
        BTN.__init__(self, master, text=text, padx=14, pady=6, font=('Verdana', 12), relief=FLAT, *args, **kwargs)

        self.color = color
        self.disabled = disabled

        self.colors = {
            'default': {
                'background': '#f5f5f5',
                'foreground': '#212121',
                'on_hover': '#e0e0e0',
                'disabled_bg': '#eeeeee',
                'disabled_fg': '#9e9e9e',
                'on_click': '#bdbdbd'},
            'info': {
                'background': '#33b5e5',
                'foreground': '#fafafa',
                'on_hover': '#0099CC',
                'disabled_bg': '#64b5f6',
                'disabled_fg': '#e0e0e0',
                'on_click': '#2196f3'},
            'primary': {
                'background': '#4285F4',
                'foreground': '#fafafa',
                'on_hover': '#0d47a1',
                'disabled_bg': '#82b1ff',
                'disabled_fg': '#e0e0e0',
                'on_click': '#01579b'}
        }

        if color:
            if color in self.colors:
                if disabled:
                    self.background_color = self.colors[color]['disabled_bg']
                    self.foreground_color = self.colors[color]['disabled_fg']
                else:
                    self.background_color = self.colors[color]['background']
                    self.foreground_color = self.colors[color]['foreground']
                self.on_hover_color = self.colors[color]['on_hover']
                self.on_click_color = self.colors[color]['on_click']
            else:
                if disabled:
                    self.background_color = self.colors['default']['disabled_bg']
                    self.foreground_color = self.colors['default']['disabled_fg']
                else:
                    self.background_color = self.colors['default']['background']
                    self.foreground_color = self.colors['default']['foreground']
                self.on_hover_color = self.colors['default']['on_hover']
                self.on_click_color = self.colors['default']['on_click']
        else:
            if disabled:
                self.background_color = self.colors['default']['disabled_bg']
                self.foreground_color = self.colors['default']['disabled_fg']
            else:
                self.background_color = self.colors['default']['background']
                self.foreground_color = self.colors['default']['foreground']
            self.on_hover_color = self.colors['default']['on_hover']
            self.on_click_color = self.colors['default']['on_click']

        if not disabled:
            self.bind('<Enter>', self.label_on_hover)
            self.bind('<Leave>', self.label_off_hover)
            self.bind('<Button-1>', lambda event: self.on_click(command))

        self.label_off_hover()

    def label_on_hover(self, *args):
        if not self.disabled:
            self.configure(bg=self.on_hover_color, cursor="hand2")

    def label_off_hover(self, *args):
        if not self.disabled:
            self.configure(bg=self.background_color, fg=self.foreground_color)

    def on_click(self, command):
        if not self.disabled:
            self.configure(bg=self.on_click_color)
            if command:
                command()

    def get_text(self):
        return self.cget('text')

    def set_text(self, text=''):
        self.config(text=text)


if __name__ == '__main__':
    pass

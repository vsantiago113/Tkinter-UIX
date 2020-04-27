from tkinter import Label
from tkinter import FLAT
from typing import NoReturn, Any, Callable


class Button(Label):
    """The Button is a custom button created using a Label widget but has the same functionality as a regular button.
All the Label methods, arguments and keyword arguments are supported as the Button is an actual Label widget"""
    def __init__(self, master: Any, text: str = '', command: (Callable, None) = None, color: str = 'default',
                 disabled: bool = False, *args: Any, **kwargs: Any):
        """

        :param Any master: The parent Window where the widget will be placed on.
        :param str text: The text of the button.
        :param command: A function to be trigger when the button is pressed.
        :type command: Callable or None
        :param str color: The available colors are - cloud, info, primary, danger, warning, success, elegant and default
        :param bool disabled: If the button is disabled it does not respond to click and it must be a bool value.
        :param Any args: Any extra arguments.
        :param Any kwargs: Any extra keyword arguments.
        """
        Label.__init__(self, master, text=text, padx=14, pady=6, font=('Verdana', 12), relief=FLAT, *args, **kwargs)

        self.disabled = disabled

        self.colors = {
            'cloud': {
                'background': '#f5f5f5',
                'foreground': '#212121',
                'on_hover': '#e0e0e0',
                'disabled_bg': '#eeeeee',
                'disabled_fg': '#9e9e9e'},
            'info': {
                'background': '#33b5e5',
                'foreground': '#fafafa',
                'on_hover': '#0099CC',
                'disabled_bg': '#64b5f6',
                'disabled_fg': '#e0e0e0'},
            'primary': {
                'background': '#4285F4',
                'foreground': '#fafafa',
                'on_hover': '#0d47a1',
                'disabled_bg': '#82b1ff',
                'disabled_fg': '#e0e0e0'},
            'danger': {
                'background': '#ff4444',
                'foreground': '#fafafa',
                'on_hover': '#CC0000',
                'disabled_bg': '#ff8a80',
                'disabled_fg': '#e0e0e0'},
            'warning': {
                'background': '#ffbb33',
                'foreground': '#fafafa',
                'on_hover': '#FF8800',
                'disabled_bg': '#f0f4c3',
                'disabled_fg': '#e0e0e0'},
            'success': {
                'background': '#00C851',
                'foreground': '#fafafa',
                'on_hover': '#007E33',
                'disabled_bg': '#a5d6a7',
                'disabled_fg': '#e0e0e0'},
            'elegant': {
                'background': '#2E2E2E',
                'foreground': '#fafafa',
                'on_hover': '#212121',
                'disabled_bg': '#757575',
                'disabled_fg': '#e0e0e0'},
            'default': {
                'background': '#2BBBAD',
                'foreground': '#fafafa',
                'on_hover': '#00695c',
                'disabled_bg': '#80cbc4',
                'disabled_fg': '#e0e0e0'}
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
            else:
                if disabled:
                    self.background_color = self.colors['default']['disabled_bg']
                    self.foreground_color = self.colors['default']['disabled_fg']
                else:
                    self.background_color = self.colors['default']['background']
                    self.foreground_color = self.colors['default']['foreground']
                self.on_hover_color = self.colors['default']['on_hover']
        else:
            if disabled:
                self.background_color = self.colors['default']['disabled_bg']
                self.foreground_color = self.colors['default']['disabled_fg']
            else:
                self.background_color = self.colors['default']['background']
                self.foreground_color = self.colors['default']['foreground']
            self.on_hover_color = self.colors['default']['on_hover']

        if not disabled:
            self.bind('<Enter>', self.label_on_hover)
            self.bind('<Leave>', self.label_off_hover)
            self.bind('<Button-1>', lambda event: self.on_click(command))

        self.label_off_hover()

    def label_on_hover(self, *args) -> NoReturn:
        """When mouse hover over the button it changes color and display a hand pointer."""
        if not self.disabled:
            self.configure(bg=self.on_hover_color, cursor="hand2")

    def label_off_hover(self, *args) -> NoReturn:
        """when mouse move away from the button it revert back to main color and default mouse pointer."""
        self.configure(bg=self.background_color, fg=self.foreground_color)

    def on_click(self, command: callable) -> NoReturn:
        """When button is clicked it triggers the function passed on the command argument."""
        if not self.disabled:
            if command:
                command()

    def get_text(self) -> str:
        """Return button text"""
        return self.cget('text')

    def set_text(self, text='') -> NoReturn:
        """Set the button text to the given value"""
        self.configure(text=text)


if __name__ == '__main__':
    pass

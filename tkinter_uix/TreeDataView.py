import tkinter as tk
from tkinter import ttk, font


class TreeDataView(tk.Frame):
    def __init__(self, master, headers, height=False, scrollbar_x=True, scrollbar_y=True, multi_select=True,
                 on_click=None, on_double_click=None, on_right_click=None, on_return_key=None, *args, **kwargs):

        tk.Frame.__init__(self, master)

        self.headers = headers
        self.multi_select = multi_select
        self.last_event = None

        def sortby(tree, col, descending):
            # Sort tree contents when a column is clicked on.
            # grab values to sort
            data = [(tree.set(child, col), child) for child in tree.get_children('')]

            # reorder data
            data.sort(reverse=descending)
            num = 'Even'
            for indx, item in enumerate(data):
                tree.move(item[1], '', indx)

            # switch the heading so that it will sort in the opposite direction
            tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

        container = tk.Frame(self)
        container.pack(fill='both', expand=True)

        if self.multi_select is None or self.multi_select is False:
            mode = 'browse'  # Select single row
        else:
            mode = 'extended'  # Select multiple rows

        style = ttk.Style()
        style.configure('mystyle.Treeview', font=('Verdana', 12))
        style.configure('mystyle.Treeview.Heading', font=('Verdana', 12))

        self.tree = ttk.Treeview(container, columns=headers, show='headings', selectmode=mode, style='mystyle.Treeview')
        vsb = ttk.Scrollbar(container, orient='vertical', command=self.tree.yview)
        hsb = ttk.Scrollbar(container, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)

        if bool(height) is True:
            self.tree.configure(height=height)
        else:
            pass
        
        if bool(scrollbar_y) is True:
            vsb.grid(column=1, row=0, sticky='ns', in_=container)
        else:
            pass
            
        if bool(scrollbar_x) is True:
            hsb.grid(column=0, row=1, sticky='ew', in_=container)
        else:
            pass

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        for col in headers:
            self.tree.heading(col, text=col, anchor='w', command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.column(col, width=font.Font().measure(col.title()))

        if on_click:
            self.tree.bind('<Button-1>', on_click)
        else:
            pass

        if on_double_click:
            self.tree.bind('<Double-Button-1>', on_double_click)
        else:
            pass

        if on_right_click:
            self.tree.bind('<Button-3>', lambda event: self.on_right_click_menu(on_right_click, event))
        else:
            pass

        if on_return_key:
            self.tree.bind('<Return>', on_return_key)
        else:
            pass
            
        for index, col in enumerate(headers):
            self.tree.column(headers[index], minwidth=50, stretch=True)

    def identify_row(self, *args, **kwargs):
        pass

    def insert(self, data):
        self.tree.insert('', 'end', values=data)
        data = None
        del data

    def clear(self): 
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_all_items(self):
        items = []
        for item in self.tree.get_children():
            items.append(self.tree.item(item, 'values'))
        return items

    def get_selected_rows(self):
        selection = self.tree.selection()
        if selection:
            items = [self.tree.item(item, 'values') for item in selection]
            return items

    def get_selected_cell(self):
        if self.last_event:
            column = self.tree.identify_column(self.last_event.x)
            selected_row = self.tree.selection()
            if len(selected_row) == 1:
                item = self.tree.item(selected_row[0], 'values')
                cell = int(column[1]) - 1
                return item[cell]

    def on_right_click_menu(self, menu, event):
        self.last_event = event
        if self.multi_select:
            menu.show(event)
        elif self.multi_select is None or self.multi_select is False:
            row_id = self.tree.identify_row(event.y)
            self.tree.selection_set(row_id)
            menu.show(event)


if __name__ == '__main__':
    pass

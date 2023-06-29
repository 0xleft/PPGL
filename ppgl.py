import os
import tkinter as tk
from PIL import ImageTk, Image

# gui class that is reusable meaning it easy
class GUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("YATP")
        self.root.resizable(True, True)
        self.root.geometry(f"{self.width}x{self.height}")
        self.statistics = {}

    def start(self):
        self.root.mainloop()

    def add_text(self, text, x, y):
        label = tk.Label(self.root, text=text)
        label.place(x=x, y=y)
        self.root.update()
        return label

    def add_button(self, text, command, x, y, w, h):
        button = tk.Button(self.root, text=text, command=command)
        button.place(x=x, y=y, width=w, height=h)
        self.root.update()
        return button

    def add_input(self, x, y, w, h, onchange=None):
        sv = None
        if onchange is not None:
            sv = tk.StringVar()
            sv.trace("w", lambda name, index, mode, sv=sv: onchange())
        entry = tk.Entry(self.root, textvariable=sv)
        entry.place(x=x, y=y, width=w, height=h)
        self.root.update()
        return entry

    def add_dropdown_menu(self, options, x, y):
        variable = tk.StringVar(self.root)
        variable.set(options[0])
        menu = tk.OptionMenu(self.root, variable, *options)
        menu.place(x=x, y=y)
        self.root.update()
        return variable

    def add_statistic(self, id, placeholder, x, y):
        self.root.update()
        self.statistics[id] = (self.add_text(placeholder, x, y))

    def update_statistic(self, id, value):
        self.statistics[id].config(text=value)
        self.root.update()

    def add_container(self, x, y):
        container = tk.Frame(self.root)
        container.place(x=x, y=y)
        self.root.update()
        return container

    def show_notification(self, text, time=5000):
        text = self.add_text(text, self.width / 2, self.height / 2)
        self.root.after(time, lambda: text.destroy())
        self.root.update()

    def add_image(self, image_path, x, y, converter):
        self.root.update()
        image = ImageTk.PhotoImage(Image.open(image_path))
        label = tk.Label(self.root, image=image)
        label.image = image
        label.place(x=x, y=y)
        label.bind("<Button-1>", lambda event: self.open_image(converter))
        self.root.update()
        return label

    def open_image(self, converter):
        image_path = converter.images[self.image_id].image_path
        os.startfile(image_path)
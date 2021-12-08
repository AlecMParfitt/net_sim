"""
    Link_Popup.py

    Creates a popup window that asks users to slecect a start and end node.

    Uses two drop down menus to select start and end nodes.

"""

from tkinter import *
from Link import Link

class Link_Popup:
    def __init__(self, parent, node_frames, window, link_count = 0):
        self.parent = parent
        self.node_frames = node_frames
        self.window = window
        self.link_count = link_count

        self.top = Toplevel(self.parent)
        self.top.title("Select start and end nodes")

        self.start_var = StringVar()
        self.start_var.set(self.node_frames[str(1)].node.name)

        self.end_var = StringVar()
        self.end_var.set(self.node_frames[str(1)].node.name)

        self.node_names = []
        for key, value in self.node_frames.items():
            self.node_names.append(value.node.name)

        self.node_dict = dict (zip(self.node_names, self.node_frames.keys()))


        self.start_label = Label(self.top, text="Start Node:")
        self.start_label.pack()
        self.start_dropdown = OptionMenu(self.top, self.start_var, *self.node_names)
        self.start_dropdown.pack()

        self.end_label = Label(self.top, text="End Node:")
        self.end_label.pack()
        self.end_dropdown = OptionMenu(self.top, self.end_var, *self.node_names)
        self.end_dropdown.pack()

        self.ok_button = Button(self.top, text="OK", command=self.ok)
        self.ok_button.pack()

    def get_link_start(self):
        return self.node_frames[self.node_dict[self.start_var.get()]]

    def get_link_end(self):
        return self.node_frames[self.node_dict[self.end_var.get()]]

    def ok(self):
        self.window.link_objects[self.link_count] = (Link(self.start_var.get(), self.end_var.get()))
        self.top.destroy()


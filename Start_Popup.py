from tkinter import *
from Message import Packet

class Start_Popup:
    def __init__(self, parent, node_frames, link_objects):
        self.parent = parent
        self.node_frames = node_frames
        self.link_objects = link_objects

        self.top = Toplevel(self.parent)
        self.top.title("Enter Data information")

        self.start_var = StringVar()
        self.start_var.set(self.node_frames[str(1)].node.name)

        self.end_var = StringVar()
        self.end_var.set(self.node_frames[str(1)].node.name)

        self.node_names = []
        for key, value in self.node_frames.items():
            self.node_names.append(value.node.name)

        self.node_dict = dict (zip(self.node_names, self.node_frames.keys()))


        self.start_label = Label(self.top, text="Sending Node:")
        self.start_dropdown = OptionMenu(self.top, self.start_var, *self.node_names)
        self.start_dropdown.pack()

        self.end_label = Label(self.top, text="Receiving Node:")
        self.end_dropdown = OptionMenu(self.top, self.end_var, *self.node_names)
        self.end_dropdown.pack()

        self.message_label = Label(self.top, text="Message Size (int):")
        self.message_entry = Entry(self.top)

        self.packet_label = Label(self.top, text="Packet Size (int):")
        self.packet_entry = Entry(self.top)





        self.ok_button = Button(self.top, text="OK", command=self.ok)
        self.ok_button.pack()

    def ok(self):
        self.start_node = self.node_frames[self.node_dict[self.start_var.get()]]
        self.end_node = self.node_frames[self.node_dict[self.end_var.get()]]

        packet_num = int(self.message_entry.get()) // int(self.packet_entry.get())


"""
    Node_Popup.py

    Node frame class for Window.py

    creates a frame with a label and a dropdown menu
    for the user to select a node from the list of predefined nodes by node_name

"""
import csv

from tkinter import *

class Node_Popup:
    def __init__(self, parent):
        self.parent = parent
        self.top = Toplevel(self.parent)

        # read node data from csv file
        nodes = self.read_nodes("predefined_nodes.csv")

        # get node names from list of nodes
        node_names = self.get_node_names(nodes)

        # make a dictionary of node names and node values
        self.node_dict = dict(zip(node_names, nodes))

        # create variable to hold node name
        self.var = StringVar()

        # set default node name to first node name in list
        self.var.set(node_names[0])

        # create dropdown menu
        self.dropdown = OptionMenu(self.top, self.var, *node_names)
        self.dropdown.pack()

        # create label
        self.label = Label(self.top, text="Select a node")
        self.label.pack()

        # create button
        self.button = Button(self.top, text="OK", command=self.top.destroy)
        self.button.pack()

        # create label for node name
        self.node_name_label = Label(self.top, textvariable=self.var)
        self.node_name_label.pack()

    # read node data from csv file
    def read_nodes(self, file_name):
        """
        read_nodes(file_name)

        reads node data from csv file and returns a list of nodes
        """
        nodes = []
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                nodes.append(row)
        return nodes

    def get_node_names(self, nodes):
        """
        returns a list of node names from a list of nodes
        """
        node_names = []
        for node in nodes:
            node_names.append(node[1])
        return node_names

    # return the node info for the selected node
    def get_node_info(self):
        """
        get_node_info()

        returns the node info for the selected node
        """
        return self.node_dict[self.var.get()]

    def show_window(self):
        self.top.mainloop()




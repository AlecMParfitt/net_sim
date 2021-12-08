"""
Window class for net_sim
"""
import tkinter as tk
from Link_Popup import Link_Popup
from Node import Node
from Node_Frame import Node_Frame
from Node_Popup import Node_Popup
from Link_Popup import Link_Popup
from Link_Line import Link_Line
from Start_Popup import Start_Popup
#from Link_Line import Link_Line
#from Link_Frame import Link_Frame
#from Link import Link

class Node_Info_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="node info", font=("Helvetica", 12))
        self.label.pack()


class Window:
    
    def __init__(self, title, width, height):
        self.images = {}
        self.image_paths = {}

        self.node_count = 0
        self.node_frames = {}
        self.node_objects = {}

        self.link_count = 0
        self.link_objects = {}
        self.link_line_objects = {}

        self.title = title
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.can_width = width/1.2
        self.can_height = height/1.2
        self.canvas = tk.Canvas(self.root, width = self.can_width, height = self.can_height)
        self.canvas.config(bg = "grey")
        self.canvas.pack()
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.add_file_menu()

        self.exit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.exit_button.pack()
        self.add_node_button = tk.Button(self.root, text="Add Node", command=self.add_node)
        self.add_node_button.pack()
        self.add_link_button = tk.Button(self.root, text="Add Link", command=self.add_link)
        self.add_link_button.pack()
        self.start_button = tk.Button(self.root, text="Start", command=self.start_sim)
        self.start_button.pack()

    # show the Node_Popup
    # create a Node object from returned values
    # add the node to the canvas
    def add_node(self):
        self.node_count += 1
        inx = self.node_count
        self.node_popup = Node_Popup(self.root)
        self.add_node_button["state"] = "disabled"
        self.root.wait_window(self.node_popup.top)
        self.add_node_button["state"] = "normal"
        node_info = self.node_popup.get_node_info()
        image_path = node_info[0]
        node_name = node_info[1]
        can_forward = node_info[2]
        self.node_objects[inx] = Node(image_path, node_name, inx, can_forward, self.node_count, self.get_node_names())
        node = self.node_objects[inx]
        self.node_frames[str(inx)] = Node_Frame(self.canvas, self.node_objects[inx], node.image_name, node.name)
        x, y = self.get_canvas_dimensions()
        self.node_frames[str(inx)].place(x=x/2, y=y/2)

    def get_node_names(self):
        return [node.name for node in self.node_objects.values()]

    def add_link(self):
        if self.link_count != 0:
            self.link_count += 1
        self.link_popup = Link_Popup(self.root, self.node_frames, self, self.link_count)
        self.add_link_button["state"] = "disabled"
        self.root.wait_window(self.link_popup.top)
        self.add_link_button["state"] = "normal"
        link_start = self.link_popup.get_link_start().get_coordinates()
        link_end = self.link_popup.get_link_end().get_coordinates()
        self.make_link(link_start, link_end, self.link_popup.get_link_start(), self.link_popup.get_link_end())


    # draw a link between given coordinates
    def make_link(self, link_start, link_end, start_node, end_node):
        x1, y1 = link_start
        x2, y2 = link_end
        x1 += 50
        y1 += 50
        x2 += 50
        y2 += 50

        new_line = Link_Line(self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=5), start_node, end_node)
        start_node.links.append(new_line)
        end_node.links.append(new_line)
        self.link_line_objects[self.link_count] = new_line
        self.canvas.pack

    def start_sim(self):
        self.start_popup = Start_Popup(self.root, self.node_frames, self.link_line_objects)
        self.start_button["state"] = "disabled"
        self.root.wait_window(self.start_popup.top)
        self.start_button["state"] = "normal"

    def find_canvas_center(self):
        """
        finds the center of the canvas
        """
        x, y = self.get_canvas_dimensions()
        return x/2, y/2


    def move_image(self, e):
        x = e.x
        y = e.y

        inx = 0
        self.add_image(inx, x, y, self.image_paths[inx])

    def add_image(self, inx, x, y, image_path):
        if image_path not in self.image_paths:
            self.image_paths[inx] = image_path
            self.images[inx] = tk.PhotoImage(file=image_path)
        self.root.image = self.images[inx]
        self.canvas.create_image(x, y, image=self.images[inx])

    # add file menu
    def add_file_menu(self):
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
    

    def open_file(self):
        pass

    def save_file(self):
        pass

    def save_file_as(self):
        pass

    def get_canvas_dimensions(self):
        return self.can_width, self.can_height

    def show_window(self):
        self.root.mainloop()
import tkinter as tk

from Link_Line import Link_Line

class DragDropMixin:
    def __init__(self, parent, links):
        self.parent = parent
        self.links = links
        self.bind("<Button-1>", self.on_start)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)
    
    def on_start(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y
        if len(self.links) > 0:
            for link in self.links:
                if self is link.start:
                    end_x, end_y = link.end.get_coordinates()
                    self.parent.coords(link.value, self.winfo_x()+50, self.winfo_y()+50, end_x+50, end_y+50)
                if self is link.end:
                    start_x, start_y = link.start.get_coordinates()
                    self.parent.coords(link.value, start_x+50, start_y+50, self.winfo_x()+50, self.winfo_y()+50)
    
    def on_drag(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)
        if len(self.links) > 0:
            for link in self.links:
                if self is link.start:
                    end_x, end_y = link.end.get_coordinates()
                    self.parent.coords(link.value, self.winfo_x()+50, self.winfo_y()+50, end_x+50, end_y+50)
                if self is link.end:
                    start_x, start_y = link.start.get_coordinates()
                    self.parent.coords(link.value, start_x+50, start_y+50, self.winfo_x()+50, self.winfo_y()+50)

    def on_release(self, event):
        widget = event.widget
        x = self.winfo_x()
        y =self.winfo_y()
    

class Node_Frame(DragDropMixin, tk.Frame):
    def __init__(self, parent, node, image_path, node_name, links = []):
        self.parent = parent
        self.links = links
        self.node = node
        tk.Frame.__init__(self, self.parent)
        super().__init__(self.parent, self.links)
        self.label = tk.Label(self, text=node_name, font=("Helvetica", 12))
        self.canvas = tk.Canvas(self, width=100, height=100, bd=0, highlightthickness=0)
        self.canvas.pack()
        image = tk.PhotoImage(file=image_path)
        self.image = image
        #place the image in the center of the canvas
        self.canvas.create_image(50, 50, image=image)
        self.label.pack()
        self.pack()

    def get_coordinates(self):
        return self.winfo_x(), self.winfo_y()


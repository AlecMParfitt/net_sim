import time

class Message():
    def __init__(self, canvas, sending_node = None, receiving_node = None, node_frames = None, link_objects = None, packet_size = 1, packet_count = 1, x_size = 5, y_size = 5, x_vel = 0, y_vel = 0, start_x = 0, start_y = 0):
        self.sending_node = sending_node
        self.canvas = canvas
        self.receiving_node = receiving_node
        self.packet_size = packet_size
        self.packet_count = packet_count
        self.packets = []
        self.node_frames = node_frames
        self.link_objects = link_objects
        self.x_size = x_size
        self.y_size = y_size
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x = 50
        self.y = 50
        self.start_x = start_x
        self.start_y = start_y
        self.image = self.canvas.create_rectangle(0, 0, self.x, self.y, fill = "white")
        self.image.coords(self.image)

    def move(self, x_vel, y_vel):
        self.canvas.move(self.image, x_vel, y_vel)
        return self.canvas.coords(self.image)


    

class Message():
    def __init__(self, sending_node, receiving_node, packet_size, packet_count, node_frames, link_objects):
        self.sending_node = sending_node
        self.receiving_node = receiving_node
        self.packet_size = packet_size
        self.packet_count = packet_count
        self.packets = []
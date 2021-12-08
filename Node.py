
class Node():
    def __init__(self, image_name, name, inx, can_forward, node_count = 0, node_names = []):
        self.image_name = image_name
        self.node_names = node_names
        if name in node_names:
            self.name = name + str(node_count)
        else:
            self.name = name
        self.inx = inx
        self.can_forward = can_forward

    
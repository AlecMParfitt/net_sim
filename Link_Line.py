
class Link_Line(int):

    def __new__(cls, value, *args, **kwargs):
        return super().__new__(cls, value)

    def __init__(self, value, start, end):
        super().__init__()
        self.value = value
        self.start = start
        self.end = end
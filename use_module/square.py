from oop.geometry_area import GeometryArea


class square(GeometryArea):
    def __init__(self, p):
        self.p = p


    def info(self):
        return f'Module calculate Square = {self.p} * {self.l} '

    def calculate_square(self):
        return self.p * self.l

class Point:
  def __init__(self, x, y): # coord -> es muy redundante, # x and y son nombres comunes para describir un punto
    self.x = x
    self.y = y


class Rectangle:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    # Metodo debe tener un nombre que describa que operacion realiza
    # def area, suena como una propiedad
    def get_area(self):
        return self.width * self.height

    def print_coordinate(self):
        top_right = self.origin.x + self.width
        bottom_left = self.origin.y + self.height
        print('Starting Point (X)): ' + str(self.origin.x))
        print('Starting Point (Y)): ' + str(self.origin.y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    origin_point = Point(50, 100)
    rectangle = Rectangle(origin_point, 90, 10)

    return rectangle


rectangle = build_rectangle()

print(rectangle.get_area())
rectangle.print_coordinate()
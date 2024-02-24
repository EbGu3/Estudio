class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Rectangle:
    def __init__(self, starting_point, width, high):
        self.starting_point = starting_point
        self.width = width
        self.high = high

    def calculate_area(self):
        return self.width * self.high
    
    def print_points(self):
        coord_x_end = self.starting_point.coord_x + self.width
        coord_y_end = self.starting_point.coord_y + self.high
        print('Starting Point (X)): ' + str(self.starting_point.coord_x))
        print('Starting Point (Y)): ' + str(self.starting_point.coord_y))
        print('End Point X-Axis (Top Right): ' + str(coord_x_end))
        print('End Point Y-Axis (Bottom Left): ' + str(coord_y_end))

main_point = Point(-50, -100)
rectangle = Rectangle(main_point, 90, 10)
print(rectangle.calculate_area())
print(rectangle.print_points())

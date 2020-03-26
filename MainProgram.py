from Rectangle import Rectangle
from Shape import Shape
from Triangle import Triangle

# for the Shape instance
shape = Shape(6,8,"Red")
print("This is just a Shape.\n")
shape.show_color()
# for the Rectangle instance
print("This is a Rectangle.\n")
rectangle = Rectangle(shape.height, shape.width, shape.color, 2)
rectangle.show_color()
rectangle.show_perimeter()
rectangle.show_border_size()
# for the Triangle instance
triangle = Triangle(shape.height, shape.width, shape.color)
print("This is a Triangle.\n")
triangle.show_color()
triangle.show_area()
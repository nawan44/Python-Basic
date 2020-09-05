#Triangles Area 1
base = 8
height = 6
triangles_area = base * height / 2
print(f'Triangles with base = {base} '
      f'and height = {height} = {triangles_area}')

#Triangles Area 2 with function
def calculate_triangles_area(base, height):
    triangles_area2 = base * height / 2
    return triangles_area2

print(calculate_triangles_area(10, 6))
print(calculate_triangles_area(4, 5))

#Square Area
def calculate_square_area(side):
    square_area = side  * side
    return square_area
print(calculate_square_area(5))

#Rectangle
def calculate_rectangle_area(length, width):
    rectangle_area = length * width
    return  rectangle_area
print(calculate_rectangle_area(6, 8))


#circle
def calculate_circle ( radius ):
    v = 22/7
    circle_area = v * radius
    return circle_area
print(calculate_circle(7))


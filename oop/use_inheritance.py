from oop.geometry_area import GeometryArea
from use_module.square import  square
from use_module.triangles import  triangle

print('Use OOP')
p1 = square(10, 3)
print(p1.info())
print(p1.calculate_square())


s1 = triangle(4, 2)
print(s1.info())
print(s1.calculat_area())

print('\n Try make object_oriented_programming with Geometry Area class')
b1 = GeometryArea()
b1.info()


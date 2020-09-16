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



geometry_area_list = []
geometry_area_list.append(p1)
geometry_area_list.append(s1)

print('\nPolypohirsm')
for geometry_area in geometry_area_list:
    print(geometry_area.info())



from Learn_package.module_square import calculate_square_area, info as  info_square
from Learn_package.module_triangle_area import calculate_triangles_area, info as info_triangles

print(info_square())
print(f'calculate square {calculate_square_area(10)}')

print(info_triangles())
print(f'calculate triangles {calculate_triangles_area(10, 3)}')

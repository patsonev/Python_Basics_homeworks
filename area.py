from math import pi

figure = input()
if figure == 'square':
    a = float(input())
    area = a * a
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == 'circle':
    radius = float(input())
    area = pi * radius ** 2
elif figure == 'triangle':
    side = float(input())
    high = float(input())
    area = side * high / 2
print(f"{area:.3f}")
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
width = abs(y1 - y2)
length = abs(x1 - x2)
area = width * length
perimeter = 2 * width + 2 * length
print(f'{area:.2f}')
print(f'{perimeter:.2f}')
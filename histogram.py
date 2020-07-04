count = int(input())

histogram = [0, 0, 0, 0, 0]

for i in range(count):
    number = int(input())
    if number == 1000:
        number = 999
    column = number // 200
    histogram[column] += 100 / count

for k in range(len(histogram)):
    print(f'{histogram[k]:.2f}%')
count = int(input())

a = 0
b = 0
c = 0

for i in range(count):
    number = int(input())
    if number % 2 == 0:
        a +=1
    if number % 3 == 0:
        b += 1
    if number % 4 == 0:
        c += 1

print(f'{a * 100 / count:.2f}% \n{b * 100 / count:.2f}% \n{c * 100 / count:.2f}%')
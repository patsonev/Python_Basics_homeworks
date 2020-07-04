first = int(input())
second = int(input())
third = int(input())

sum = first + second + third

minutes = sum // 60
seconds = sum % 60

print(f'{minutes}:{seconds:02d}')
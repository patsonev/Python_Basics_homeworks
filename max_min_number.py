count = int(input())

first_number = int(input())
max_number = first_number
min_number = first_number

for i in range(count-1):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
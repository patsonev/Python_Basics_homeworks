count = int(input())

first_number = int(input())
max_number = first_number
sum_numbers = 0

for i in range(1, count):
    number = int(input())
    if number > max_number:
        max_number = number
    sum_numbers += number

if sum_numbers + first_number - max_number == max_number:
    print(f'Yes \nSum = {max_number}')
else:
    print(f'No \nDiff = {abs(sum_numbers + first_number - 2 * max_number)}')

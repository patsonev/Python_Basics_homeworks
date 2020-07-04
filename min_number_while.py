count_numbers = int(input())

first_number = int(input())
counter = 0
min_number = first_number

while counter < count_numbers - 1:
    number = int(input())
    if number < min_number:
        min_number = number
    counter += 1

print(min_number)
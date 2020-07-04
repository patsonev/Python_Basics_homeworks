count_numbers = int(input())

first_number = int(input())
counter = 0
max_number = first_number

while counter < count_numbers - 1:
    number = int(input())
    if number > max_number:
        max_number = number
    counter += 1

print(max_number)
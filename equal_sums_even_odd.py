first_number = int(input())
second_number = int(input())

sum_odd = 0
sum_even = 0

for number in range(first_number, second_number + 1):
    number_to_string = str(number)
    for i in range(0, len(number_to_string)):
        if i % 2 == 1:
            sum_odd += int(number_to_string[i])
        else:
            sum_even += int(number_to_string[i])

    if sum_even == sum_odd:
        print(number, end=" ")
    sum_even = 0
    sum_odd = 0
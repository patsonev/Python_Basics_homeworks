command = ' '

sum_prime_numbers = 0
sum_nonprime_numbers = 0
counter = 0

while command != 'stop':
    command = input()
    if command == 'stop':
        break
    number = int(command)
    if number < 0:
        print('Number is negative.')
    else:
        for i in range(2, number):
            remaining = number % i
            if remaining == 0:
                counter += 1
        if counter == 0:
            sum_prime_numbers += number
        else:
            sum_nonprime_numbers += number
        counter = 0

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f'Sum of all non prime numbers is: {sum_nonprime_numbers}')

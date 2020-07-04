n = int(input())

if n <= 9:
    for number in range(1111, 1111 * n + 1):
        counter = 0
        number_to_string = str(number)
        if '0' in number_to_string:
            pass
        else:
            for position in range(3, -1, -1):
                digit = int(number_to_string[position])
                if n % digit != 0:
                    break
                if counter == 3:
                    print(number, end=' ')
                    break
                counter += 1

else:
    for number in range(1111, 10000):
        counter = 0
        number_to_string = str(number)
        if '0' in number_to_string:
            pass
        else:
            for position in range(3, -1, -1):
                digit = int(number_to_string[position])
                if n % digit != 0:
                    break
                if counter == 3:
                    print(number, end=' ')
                    break
                counter += 1
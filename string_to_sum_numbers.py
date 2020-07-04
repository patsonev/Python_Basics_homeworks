string = input()
n = len(string)

sum_numbers = 0

for i in range(1, n + 1):
    if string[i - 1] == 'a':
        sum_numbers += 1
    elif string[i - 1] == 'e':
        sum_numbers += 2
    elif string[i - 1] == 'i':
        sum_numbers += 3
    elif string[i - 1] == 'o':
        sum_numbers += 4
    elif string[i - 1] == 'u':
        sum_numbers += 5
    else:
        pass

print(sum_numbers)

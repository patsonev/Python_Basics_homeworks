alphabet = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
l = int(input())

for first in range(1, n + 1):
    for second in range(1, n + 1):
        for third in range(0, l):
            for fourth in range(0, l):
                for fifth in range(0, n + 1):
                    if fifth > first and fifth > second:
                        print(f'{first}{second}{alphabet[third]}{alphabet[fourth]}{fifth}', end=" ")
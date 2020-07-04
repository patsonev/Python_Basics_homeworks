sum_steps = 0

while sum_steps < 1e4:
    command = input()
    if command != 'Going home':
        steps = int(command)
        sum_steps += steps
    else:
        steps = int(input())
        sum_steps += steps
        break

if sum_steps >= 1e4:
    print(f'Goal reached! Good job!')
else:
    print(f'{10000 - sum_steps} more steps to reach goal.')
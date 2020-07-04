width = int(input())
length = int(input())
high = int(input())

free_space = width * length * high
command = input()

while command != 'Done':
    boxes = int(command)
    free_space -= boxes
    if free_space <= 0:
        print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
        break
    command = input()

if command == 'Done':
    print(f'{free_space} Cubic meters left.')
cake_width = int(input())
cake_length = int(input())

size_cake = cake_width * cake_length

while size_cake > 0:
    command = input()
    if command != 'STOP':
        pieces = int(command)
        size_cake -= pieces
    else:
        print(f'{abs(size_cake)} pieces are left.')
        break

if size_cake < 0:
    print(f'No more cake left! You need {abs(size_cake)} pieces more.')
elif size_cake == 0:
    print(f'{abs(size_cake)} pieces are left.')
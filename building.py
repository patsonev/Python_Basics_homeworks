count_floors = int(input())
count_apartments = int(input())

counter = 0

for floor in range(count_floors, 0, -1):
    for apartment in range(0, count_apartments):
        if floor == count_floors:
            print(f'L{floor}{apartment}', end=' ')
            counter += 1
            if counter == count_apartments:
                print('\t')
                counter = 0
        elif floor % 2 == 1:
            print(f'A{floor}{apartment}', end=' ')
            counter += 1
            if counter == count_apartments:
                print('\t')
                counter = 0
        elif floor % 2 == 0:
            print(f'O{floor}{apartment}', end=' ')
            counter += 1
            if counter == count_apartments:
                print('\t')
                counter = 0
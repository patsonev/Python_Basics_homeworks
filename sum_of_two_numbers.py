starting_number = int(input())
ending_number = int(input())
magical_number = int(input())

counter = 0
second_counter = 0

for n1 in range(starting_number, ending_number + 1):
    for n2 in range(starting_number, ending_number + 1):
        counter += 1
        if n1 + n2 == magical_number:
            second_counter += 1
            print(f'Combination N:{counter} ({n1} + {n2} = {magical_number})')
            break
    if second_counter !=0:
        break

if second_counter == 0:
    print(f'{counter} combinations - neither equals {magical_number}')
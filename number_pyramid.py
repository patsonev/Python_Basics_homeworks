n = int(input())

counter = 1
is_counter_bigger_than_n = False

for rows in range(1, n + 1):
    for columns in range(1, rows + 1):
        if counter > n:
            is_counter_bigger_than_n = True
            break
        print(counter, end=" ")
        counter += 1
    if is_counter_bigger_than_n:
        break
    print()
for i in range(100000000):
    saved_money = 0
    destination = input()
    if destination == 'End':
        break
    needed_money = float(input())
    while saved_money < needed_money:
        money_io = float(input())
        saved_money += money_io
    saved_money -= needed_money
    print(f'Going to {destination}!')
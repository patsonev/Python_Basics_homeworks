price_vacation = float(input())
saved_money = float(input())

counter_days = 0
counter_total_days = 0

while counter_days < 5:
    action = input()
    last_action = action
    money_io = float(input())
    counter_total_days += 1
    if action == 'spend':
        if saved_money < money_io:
            saved_money = 0
        else:
            saved_money -= money_io
        if last_action == 'spend':
            counter_days += 1
    else:
        saved_money += money_io
        counter_days = 0
        if saved_money >= price_vacation:
            break

if counter_days == 5:
    print(f"You can't save the money.")
    print(counter_total_days)
else:
    print(f'You saved the money for {counter_total_days} days.')
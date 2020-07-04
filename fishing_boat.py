budget = int(input())
season = input()
count_fishmen = int(input())

price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if count_fishmen <= 6:
    price = 0.9 * price
elif 7 <= count_fishmen <= 11:
    price = 0.85 * price
elif count_fishmen >= 12:
    price = 0.75 * price

if season != 'Autumn' and count_fishmen % 2 == 0:
    price = 0.95 * price

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
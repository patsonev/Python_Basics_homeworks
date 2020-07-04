days = int(input())
room = input()
ocenka = input()

nights = days - 1

price = 0
total_price = 0

if room == 'room for one person':
    price = 18
    total_price = nights * price
    if ocenka == 'positive':
        total_price += 0.25 * total_price
    elif ocenka == 'negative':
        total_price -= 0.1 * total_price
    print(f'{total_price:.2f}')

elif room == 'apartment':
    price = 25
    total_price = nights * price
    if days < 10:
        total_price -= 0.3 * total_price
    elif days >= 10 and days <= 15:
        total_price -= 0.35 * total_price
    else:
        total_price -= 0.5 * total_price
    if ocenka == 'positive':
        total_price += 0.25 * total_price
    elif ocenka == 'negative':
        total_price -= 0.1 * total_price
    print(f'{total_price:.2f}')

elif room == 'president apartment':
    price = 35
    total_price = nights * price
    if days < 10:
        total_price -= 0.1 * total_price
    elif days >= 10 and days <= 15:
        total_price -= 0.15 * total_price
    else:
        total_price -= 0.2 * total_price
    if ocenka == 'positive':
        total_price += 0.25 * total_price
    elif ocenka == 'negative':
        total_price -= 0.1 * total_price
    print(f'{total_price:.2f}')

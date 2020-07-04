flowers = input()
count_flowers = int(input())
budget = int(input())

price = 0

if flowers == 'Roses':
    price = 5
    if count_flowers > 80:
        price = 0.9 * price

elif flowers == 'Dahlias':
    price = 3.8
    if count_flowers > 90:
        price = 0.85 * price

elif flowers == 'Tulips':
    price = 2.8
    if count_flowers > 80:
        price = 0.85 * price

elif flowers == 'Narcissus':
    price = 3
    if count_flowers < 120:
        price = 1.15 * price

elif flowers == 'Gladiolus':
    price = 2.5
    if count_flowers < 80:
        price = 1.2 * price

if price * count_flowers <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {flowers} and {budget - price * count_flowers:.2f} leva left.")
else:
    print(f"Not enough money, you need {price * count_flowers - budget:.2f} leva more.")

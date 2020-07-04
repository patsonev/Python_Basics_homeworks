ages = int(input())
price_peralnq = float(input())
price_toy = int(input())

suma = 0
money = 0

for i in range(1, ages + 1):
    if i % 2 == 0:
        money += 10
        suma += money - 1
    if i % 2 == 1:
        suma += price_toy

if suma >= price_peralnq:
    print(f'Yes! {suma - price_peralnq:.2f}')
else:
    print(f'No! {price_peralnq - suma:.2f}')

projection_type = input()
r = int(input())
c = int(input())

price = 0

if projection_type == 'Premiere':
    price = 12
elif projection_type == 'Normal':
    price = 7.5
elif projection_type == 'Discount':
    price = 5

total_income = price * r * c
print(f'{total_income:.2f} leva')

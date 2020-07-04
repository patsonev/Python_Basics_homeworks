month = input()
count = int(input())

price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_studio = 50
    if 7 < count <= 14:
        price_studio = price_studio * 0.95
    elif count > 14:
        price_studio = price_studio *0.7
    price_apartment = 65

elif month == 'June' or month == 'September':
    price_studio = 75.2
    if count > 14:
        price_studio = price_studio * 0.8
    price_apartment = 68.7

elif month == 'July' or month == 'August':
    price_apartment = 77
    price_studio = 76

if count > 14:
    price_apartment = price_apartment * 0.9

print(f"Apartment: {count * price_apartment:.2f} lv.")
print(f"Studio: {count * price_studio:.2f} lv.")
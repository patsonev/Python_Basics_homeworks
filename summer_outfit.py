degrees = int(input())
vreme_ot_denonoshtieto = input()

outfit = ''
shoes = ''

if 10 <= degrees <= 18:
    if vreme_ot_denonoshtieto == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif vreme_ot_denonoshtieto == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif vreme_ot_denonoshtieto == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif 18 < degrees <= 24:
    if vreme_ot_denonoshtieto == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif vreme_ot_denonoshtieto == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif vreme_ot_denonoshtieto == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif degrees >= 25:
    if vreme_ot_denonoshtieto == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif vreme_ot_denonoshtieto == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif vreme_ot_denonoshtieto == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
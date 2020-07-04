biudjet = float(input())
broi_statisti = int(input())
edinichna_cena_obleklo = float(input())

cena_dekor = 0.1 * biudjet
obshta_cena_obleklo = edinichna_cena_obleklo * broi_statisti

if broi_statisti > 150:
    obshta_cena_obleklo = obshta_cena_obleklo * 0.9

if cena_dekor + obshta_cena_obleklo <= biudjet:
    ostavashti = biudjet - obshta_cena_obleklo - cena_dekor
    print('Action!')
    print(f'Wingard starts filming with {ostavashti:.2f} leva left.')
else:
    nedostig = cena_dekor + obshta_cena_obleklo - biudjet
    print('Not enough money!')
    print(f'Wingard needs {nedostig:.2f} leva more.')
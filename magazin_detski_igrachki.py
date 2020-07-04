cena_ekskurziq = float(input())
broi_pyzeli = int(input())
broi_govoreshti_kukli = int(input())
broi_mecheta = int(input())
broi_minioni = int(input())
broi_kamioncheta = int(input())

broi_igrachki = broi_govoreshti_kukli + broi_kamioncheta + broi_mecheta + broi_minioni + broi_pyzeli

cena_pyzeli = 2.60 * broi_pyzeli
cena_govoreshti_kukli = 3 * broi_govoreshti_kukli
cena_mecheta = 4.1 * broi_mecheta
cena_minioni = 8.2 * broi_minioni
cena_kamioncheta = 2 * broi_kamioncheta

cena_igrachki = cena_govoreshti_kukli + cena_kamioncheta + cena_mecheta + cena_minioni + cena_pyzeli

if broi_igrachki >= 50:
    cena_igrachki = cena_igrachki * 0.75 * 0.9
    ostavashti_pari = cena_igrachki - cena_ekskurziq
    if ostavashti_pari >= 0:
        print(f'Yes! {ostavashti_pari:.2f} lv left.')
    else:
        print(f'Not enough money! {-ostavashti_pari:.2f} lv needed.')
else:
    cena_igrachki = cena_igrachki * 0.9
    ostavashti_pari = cena_igrachki - cena_ekskurziq
    if ostavashti_pari >= 0:
        print(f'Yes! {ostavashti_pari:.2f} lv left.')
    else:
        print(f'Not enough money! {-ostavashti_pari:.2f} lv needed.')
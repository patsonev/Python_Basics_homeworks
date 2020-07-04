num_tables = int(input())
length = float(input())
width = float(input())
kare_plosht = length * length / 4
pokrivka_plosht = (length + 0.6) * (width + 0.6)
cena_kare_usd = num_tables * kare_plosht * 9
cena_kare_lv = cena_kare_usd * 1.85
cena_pokrivka_usd = num_tables * pokrivka_plosht * 7
cena_pokrivka_lv = cena_pokrivka_usd * 1.85
cena_usd = cena_kare_usd + cena_pokrivka_usd
cena_lv = cena_kare_lv + cena_pokrivka_lv
print(f'{cena_usd:.2f} USD')
print(f'{cena_lv:.2f} BGN')
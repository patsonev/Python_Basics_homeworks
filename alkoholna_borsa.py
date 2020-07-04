cena_uiski = float(input())
bira = float(input())
vino = float(input())
rakiq = float(input())
uiski = float(input())
cena_rakiq = cena_uiski / 2
cena_vino = cena_rakiq - 0.4 * cena_rakiq
cena_bira = cena_rakiq - 0.8 * cena_rakiq
obshto_cena = bira * cena_bira + vino * cena_vino + rakiq * cena_rakiq + uiski * cena_uiski
print(f'{obshto_cena:.2f}')
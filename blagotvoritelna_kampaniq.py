dni = int(input())
sladkari = int(input())
torti = int(input())
gofreti = int(input())
palachinki = int(input())
pari = (torti * 45 + gofreti * 5.8 + palachinki * 3.2) * sladkari * dni
dareni = pari - pari / 8
print(f'{dareni:.2f}')
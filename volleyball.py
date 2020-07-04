vid_godina = input()
broi_praznici = int(input())
broi_uikendi_pytuva = int(input())

broi_uikendi_sofia = 48 - broi_uikendi_pytuva
igri_sofiq = broi_uikendi_sofia * 3 / 4
igri_praznici = broi_praznici * 2 / 3
igri_roden_grad = broi_uikendi_pytuva

obshto_igri = igri_praznici + igri_roden_grad + igri_sofiq

if vid_godina == 'leap':
    obshto_igri += 0.15 * obshto_igri

print(int(obshto_igri))
dohodi = float(input())
sreden_uspeh = float(input())
minimalna_zaplata = float(input())

if dohodi < minimalna_zaplata and sreden_uspeh > 4.5:
    socialna_stipendiq = 0.35 * minimalna_zaplata
    if sreden_uspeh > 5.5:
        stipendiq_uspeh = sreden_uspeh * 25
        if stipendiq_uspeh < socialna_stipendiq:
            print(f'You get a Social scholarship {int(socialna_stipendiq)} BGN')
        else:
            print(f'You get a scholarship for excellent results {int(stipendiq_uspeh)} BGN')
    else:
        print(f'You get a Social scholarship {int(socialna_stipendiq)} BGN')
elif dohodi >= minimalna_zaplata and sreden_uspeh >= 5.5:
    stipendiq_uspeh = sreden_uspeh * 25
    print(f'You get a scholarship for excellent results {int(stipendiq_uspeh)} BGN')
else:
   print('You cannot get a scholarship!')
city = input()
sells = float(input())

commissions = 0

if city == 'Sofia':
    if sells <= 500 and sells >= 0:
        commissions = 0.05 * sells
    elif sells <= 1000 and sells > 500:
        commissions = 0.07 * sells
    elif sells > 1000 and sells <= 10000:
        commissions = 0.08 * sells
    elif sells > 10000:
        commissions = 0.12 * sells
    else:
        print('error')

elif city == 'Varna':
    if sells <= 500 and sells >= 0:
        commissions = 0.045 * sells
    elif sells <= 1000 and sells > 500:
        commissions = 0.075 * sells
    elif sells > 1000 and sells <= 10000:
        commissions = 0.1 * sells
    elif sells > 10000:
        commissions = 0.13 * sells
    else:
        print('error')

elif city == 'Plovdiv':
    if sells <= 500 and sells >= 0:
        commissions = 0.055 * sells
    elif sells <= 1000 and sells > 500:
        commissions = 0.08 * sells
    elif sells > 1000 and sells <= 10000:
        commissions = 0.12 * sells
    elif sells > 10000:
        commissions = 0.145 * sells
    else:
        print('error')

else:
    print('error')

if commissions !=0:
    print(f'{commissions:.2f}')
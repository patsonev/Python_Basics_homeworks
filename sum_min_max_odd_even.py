count = int(input())
if count != 0:
    first_number = float(input())
    oddsum = first_number
    oddmin = first_number
    oddmax = first_number
else:
    pass

if count > 1:
    second_number = float(input())
    evensum = second_number
    evenmin = second_number
    evenmax = second_number
else:
    pass

for i in range(1, count - 1):
    number = float(input())
    if i % 2 == 1:
        oddsum += number
        if oddmax < number:
            oddmax = number
        if oddmin > number:
            oddmin = number
    else:
        evensum += number
        if evenmax < number:
            evenmax = number
        if evenmin > number:
            evenmin = number

if count > 1:
    print(f'OddSum={oddsum:.2f},')
    print(f'OddMin={oddmin:.2f},')
    print(f'OddMax={oddmax:.2f},')
    print(f'EvenSum={evensum:.2f},')
    print(f'EvenMin={evenmin:.2f},')
    print(f'EvenMax={evenmax:.2f}')

elif count == 1:
    print(f'OddSum={oddsum:.2f},')
    print(f'OddMin={oddmin:.2f},')
    print(f'OddMax={oddmax:.2f},')
    print(f'EvenSum=0.00,')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')

else:
    print(f'OddSum=0.00,')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum=0.00,')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
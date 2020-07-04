distance = float(input())
from_metric = input()
to_metric = input()

if from_metric == 'm':
    if to_metric == 'm':
        print(f'{distance:.3f}')
    elif to_metric == 'cm':
        distance_cm = distance * 100
        print(f'{distance_cm:.3f}')
    elif to_metric == 'mm':
        distance_mm = distance * 1000
        print(f'{distance_mm:.3f}')

elif from_metric == 'cm':
    if to_metric == 'cm':
        print(f'{distance:.3f}')
    elif to_metric == 'm':
        distance_cm = distance / 100
        print(f'{distance_cm:.3f}')
    elif to_metric == 'mm':
        distance_mm = distance * 10
        print(f'{distance_mm:.3f}')

elif from_metric == 'mm':
    if to_metric == 'mm':
        print(f'{distance:.3f}')
    elif to_metric == 'cm':
        distance_cm = distance / 10
        print(f'{distance_cm:.3f}')
    elif to_metric == 'm':
        distance_mm = distance / 1000
        print(f'{distance_mm:.3f}')
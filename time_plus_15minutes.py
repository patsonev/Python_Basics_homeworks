hours = int(input())
minutes = int(input())

if minutes < 45:
    minutes = minutes + 15
else:
    minutes = (minutes + 15) % 60
    hours = hours + 1
    if hours >= 24:
        hours = hours % 24
print(f'{hours}:{minutes:02d}')
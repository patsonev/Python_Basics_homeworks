resto = float(input())
count = 0

while resto > 0:
    resto = round(resto, 2)
    if resto >= 2:
        resto -= 2
        count += 1
    elif resto >= 1:
        resto -= 1
        count += 1
    elif resto >= 0.5:
        resto -= 0.5
        count += 1
    elif resto >= 0.2:
        resto -= 0.2
        count += 1
    elif resto >= 0.1:
        resto -= 0.1
        count += 1
    elif resto >= 0.05:
        resto -= 0.05
        count += 1
    elif resto >= 0.02:
        resto -= 0.02
        count += 1
    elif resto >= 0.01:
        resto -= 0.01
        count += 1

print(count)

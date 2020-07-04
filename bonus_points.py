start_points = int(input())

if start_points <= 100:
    bonus_points = 5
elif start_points > 1000:
    bonus_points = start_points * 0.1
else:
    bonus_points = start_points * 0.2

if start_points % 2 == 0:
    additional_bonus = 1
else:
    additional_bonus = 0
if (start_points / 5) % 2 == 1:
    also_bonus = 2
else:
    also_bonus = 0

print(f'{additional_bonus + also_bonus + bonus_points}')
print((f'{additional_bonus + also_bonus + start_points + bonus_points}'))
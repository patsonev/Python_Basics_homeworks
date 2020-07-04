budget = float(input())
season = input()

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        cost = 0.3 * budget
        place = 'Camp'
    elif season == 'winter':
        cost = 0.7 * budget
        place = 'Hotel'

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        cost = 0.4 * budget
        place = 'Camp'
    elif season == 'winter':
        cost = 0.8 * budget
        place = 'Hotel'

elif budget > 1000:
    destination = 'Europe'
    cost = 0.9 * budget
    place = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{place} - {cost:.2f}")
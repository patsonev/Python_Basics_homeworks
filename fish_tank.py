length = int(input())
width = int(input())
high = int(input())
percent_of_volume = float(input())
percent = percent_of_volume / 100
tank_volume = length * width * high * 0.001
water_volume = tank_volume - percent * tank_volume
print(f'{water_volume:.3f}')
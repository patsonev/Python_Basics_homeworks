record = float(input())
distance = float(input())
time_one_meter = float(input())

zabavqne = (distance // 15) * 12.5
ivan_time = distance * time_one_meter + zabavqne

if record <= ivan_time:
    print(f'No, he failed! He was {ivan_time - record:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')
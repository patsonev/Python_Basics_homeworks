speed = float(input())

if speed <= 10:
    print('slow')
elif 10 < speed <= 50:
    print('average')
elif speed > 50 and speed <= 150:
    print('fast')
elif speed > 1000:
   print('extremely fast')
else:
    print('ultra fast')
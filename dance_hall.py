length = float(input())
width = float(input())
a = float(input())
whole_area = length * width * 10000
garderob = a * a * 10000
skameika = whole_area / 10
clear_area = whole_area - garderob - skameika
broi_tanciori = clear_area / (7000 + 40)
print(int(broi_tanciori))
count = int(input())

odd_sum = 0
even_sum = 0

for i in range(count):
    number = int(input())
    if i % 2 == 0:
        odd_sum += number
    if i % 2 == 1:
        even_sum += number

if even_sum == odd_sum:
    print(f'Yes \nSum = {even_sum}')
else:
    print(f'No \nDiff = {abs(even_sum - odd_sum)}')
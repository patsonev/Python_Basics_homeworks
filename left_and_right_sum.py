count = int(input())

left_sum = 0
right_sum = 0

for i in range(2*count):
    number = int(input())
    if i < count:
        left_sum += number
    if i >= count:
        right_sum += number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')
name = input()

sum_grade = 0
counter = 1
i = 0

while counter <= 12:
    grade = float(input())
    if grade >= 4:
        sum_grade += grade
        counter += 1
    else:
        i += 1
        if i > 1:
            print(f'{name} has been excluded at {counter} grade')
            break

if counter == 13:
    print(f'{name} graduated. Average grade: {sum_grade / 12:.2f}')

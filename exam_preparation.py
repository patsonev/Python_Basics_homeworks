number_weak_grade = int(input())

counter_problems = 0
counter_weak_grade = 0
sum_grade = 0

while counter_weak_grade < number_weak_grade:
    command = input()
    if command != 'Enough':
        exercise_name = command
        grade = int(input())
        sum_grade += grade
        counter_problems += 1
        if grade <= 4:
            counter_weak_grade += 1
    else:
        break

if counter_weak_grade == number_weak_grade:
    print(f'You need a break, {number_weak_grade} poor grades.')
else:
    print(f'Average score: {sum_grade / counter_problems:.2f}\nNumber of problems: {counter_problems}\nLast problem: {exercise_name}')
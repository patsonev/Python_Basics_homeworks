is_finished = True
count_trainers = int(input())

counter_means = 0
sum_mean = 0

while is_finished:
    name_presentation = input()
    sum_grade = 0
    if name_presentation == 'Finish':
        is_finished = False
        mean_presentations = sum_mean / counter_means
        print(f"Student's final assessment is {mean_presentations:.2f}.")
        break
    for i in range(0, count_trainers):
        grade = float(input())
        sum_grade += grade
    mean = sum_grade / count_trainers
    sum_mean += mean
    counter_means += 1
    print(f'{name_presentation} - {mean:.2f}.')
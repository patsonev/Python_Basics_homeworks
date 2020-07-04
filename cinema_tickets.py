counter_total = 0
counter_kid = 0
counter_standard = 0
counter_student = 0
sum_tickets = 0

movie = ''
kind_of_ticket = ''

while kind_of_ticket != 'Finish':
    movie = input()
    if movie == 'Finish':
        break
    total_seats = int(input())
    kind_of_ticket = ''
    while kind_of_ticket != 'End':
        kind_of_ticket = input()
        if kind_of_ticket == 'End':
            break
        counter_total += 1
        if kind_of_ticket == 'kid':
            counter_kid += 1
        elif kind_of_ticket == 'standard':
            counter_standard += 1
        elif kind_of_ticket == 'student':
            counter_student += 1
        if counter_total == total_seats:
            break
    print(f'{movie} - {counter_total * 100 / total_seats:.2f}% full.')
    sum_tickets += counter_total
    counter_total = 0

print(f'Total tickets: {sum_tickets}')
print(f'{counter_student * 100 / sum_tickets:.2f}% student tickets.')
print(f'{counter_standard * 100 / sum_tickets:.2f}% standard tickets.')
print(f'{counter_kid * 100 / sum_tickets:.2f}% kids tickets.')
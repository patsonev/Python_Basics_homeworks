searched_book = input()
number_of_books = int(input())

counter = 0

while counter < number_of_books:
    command = input()
    if command == searched_book:
        print(f'You checked {counter} books and found it.')
        break
    counter += 1


if counter >= number_of_books:
    print(f'The book you search is not here! \nYou checked {counter} books.')
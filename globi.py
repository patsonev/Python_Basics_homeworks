count = int(input())

salary = int(input())

for i in range(count):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
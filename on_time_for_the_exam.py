exam_start_hour = int(input())
exam_start_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

if exam_start_hour == arrival_hour:
    if 0 <= exam_start_minute - arrival_minute <= 30:
        print('On time')
        if exam_start_minute - arrival_minute != 0:
            print(f"{exam_start_minute - arrival_minute} minutes before the start")
    elif exam_start_minute < arrival_minute:
        print('Late')
        print(f"{arrival_minute - exam_start_minute} minutes after the start")
    else:
        print('Early')
        print(f"{exam_start_minute - arrival_minute:02d} minutes before the start")

elif exam_start_hour < arrival_hour:
    print('Late')
    if -60 < arrival_minute - exam_start_minute < 0:
        print(f"{arrival_minute - exam_start_minute + 60} minutes after the start")
    else:
        print(f"{arrival_hour - exam_start_hour}:{arrival_minute - exam_start_minute:02d} hours after the start")

else:
    if exam_start_hour == arrival_hour + 1:
        if exam_start_minute - arrival_minute + 60 <= 30:
            print('On time')
            print(f"{exam_start_minute - arrival_minute + 60} minutes before the start")
        else:
            print('Early')
            if 30 < exam_start_minute - arrival_minute + 60 < 60:
                print(f"{exam_start_minute - arrival_minute + 60:02d} minutes before the start")
            else:
                print(f"1:{(exam_start_minute - arrival_minute + 60) % 60:02d} hours before the start")
    else:
        print('Early')
        if exam_start_minute >= arrival_minute:
            print(f"{exam_start_hour - arrival_hour}:{exam_start_minute - arrival_minute:02d} hours before the start")
        else:
            print(
                f"{exam_start_hour - arrival_hour - 1}:{(exam_start_minute - arrival_minute + 60) % 60:02d} hours before the start")
import winsound
import datetime
import time

alarm_time_hour = int(input("Enter alarm hour: "))
alarm_time_minute = int(input("Enter alarm minute: "))
today = datetime.date.today()
current_datetime = datetime.datetime.now()
target_datetime = datetime.datetime(today.year, today.month, today.day, alarm_time_hour, alarm_time_minute)

while True:
    if current_datetime >= target_datetime :
        print("alarm has passed!")
        for i in range(6):
            winsound.Beep(1000, 500)
        break
    else:
        current_datetime = datetime.datetime.now()
        print(current_datetime.strftime("%H:%M:%S"))
        time.sleep(1)

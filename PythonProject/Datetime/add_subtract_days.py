import datetime

today = datetime.date.today()
lastDate =today - datetime.timedelta(days=8)
laterDate = today + datetime.timedelta(days=8)

print("Today date", today)
print("Before eight days", lastDate)
print("after eight days", laterDate)

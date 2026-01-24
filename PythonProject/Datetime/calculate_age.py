import datetime

dob = datetime.date(2020, 12, 12)
today = datetime.date.today()

age = today.year - dob.year
day_of_dob = dob.strftime("%A")

if age > 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

print("you age is", age)
print("your day of birth is", day_of_dob)

from datetime import date, time, datetime
today= date.today()
now=datetime.now()
print("Todays date is:", today)
print("Time is:", now)
print("Date components:", today.year, today.month, today.day)
#Return the year and name of weekday
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#Display the name of the month:
x = datetime.datetime(2023, 12, 1)
print(x.strftime("%B"))

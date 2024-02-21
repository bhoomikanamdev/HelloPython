

'''year = int(input("Input a year"))
month = int(input("Input a month"))
day = int(input("Input a Day"))
if (day >=1 and day <=30)(month in range ) :
    day_new =day + 1
elif day == 31:
    day_new = 1
    month = month + 1
elif month in range(1,12):

else:
    print("Invalid date")

print ("The next date is " + str(day_new) + "/" + str(month) +"/" + str(year))'''

'''year = eval(input("enter a year"))
month = eval(input("enter a month))
day = eval(input("enter a Day"))
if date >=1 or date <=30:
    date +=date
elif date == 31:
    date += date and month +=month
else:
    print("Invalid date")

print ("The next date is " + str (date))'''

year = int(input("year"))
month = int(input("month"))
day = int(input("day"))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
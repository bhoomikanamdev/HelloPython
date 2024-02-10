

year = int(input("Input a year"))
month = int(input("Input a month"))
day = int(input("Input a Day"))
if (day >=1 and day <=30),(month in range ), :
    day_new =day + 1
elif day == 31:
    day_new = 1
    month = month + 1
elif month in range(1,12):

else:
    print("Invalid date")

print ("The next date is " + str(day_new) + "/" + str(month) +"/" + str(year))
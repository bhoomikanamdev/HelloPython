month=input()
if month == "February":
  print ("28/29 days")
elif month in ["January","March","May","July","August","October","December"]:
  print("31 days")
elif month in ["April","June","September","November"]:
  print("30 days")
else:
  print("wrong")
temperatures_w1 = [32, 34, 31, 30, 29, 28, 33]
temperatures_w2 = [31, 34, 35, 28, 29]
sum1=0
sum2=0

# Calculate the sum of all temperatures
for temperature in temperatures_w1:
  sum1 = sum1 + temperature

for temp in temperatures_w2:
  sum2 = sum2 + temp

average1 = sum1/len(temperatures_w1)
average2 = sum2/len(temperatures_w2)

# Output the result
print("The average temperature of the week one is "+  str(average1) +" degrees Celsius.")
print("The average temperature of the week two is "+  str(average2) +" degrees Celsius.")
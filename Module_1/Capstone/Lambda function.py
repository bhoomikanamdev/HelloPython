from functools import reduce

# Create a list of numbers from 1 to 10

# Write your code here
numbers = list(range(1, 11))
#requires_output= [number**2 for number in numbers if number%2 !=0]
required_op=list[filter(lambda num:num%2 != 0,num**2)]
print(required_op)

#while
'''number1 = int(input())
input_length=len(str(number1))
print(input_length)
while input_length>=1:
    print(input_length)
    input_length=input_length-1'''

#split
my_str= "bhoomi/ka"
print(my_str.split('/'))

#sum
numbers = [1, 2, 3, 4, 5, 1, 4, 5]
Sum = sum(numbers)
print(Sum)

#range
print(*range(1,100,5))
print(type(range(1,100,5)))
print(list(range(1,100,5)))
print(list(7568))

#find sum of digits of input number
sum=0
    for val in str(784):
        sum = sum+int(val)
    print(sum)

#how to create list from number

strs = input()
for chars in strs:
  if len(chars[i])  is in [ 2,3,5,7,11]:
    print ( chars)

  else:
    continue

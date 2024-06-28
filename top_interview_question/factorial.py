'''def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

user_input = int(input())
print(fact(user_input))'''

num = int(input("Enter a number: "))
# 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   # 5040
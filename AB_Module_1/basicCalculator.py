num1 = input("enter your 1st no :")
num2 = input("enter your second no :")
operation = input ("Choose operation :")

Add = int(num1)+int(num2)
Sub = int(num1)-int(num2)
Multiply = int(num1)*int(num2)
Divide = int(num1)/int(num2)
if operation == Add:
    print (Add)
else:
    print ("Result is " + str (Sub))
def calculator (num1,num2,operation):
    if operation == 'addition':
        result = num1+num2
    elif operation == 'substraction':
        result = num1-num2
    elif operation == 'multiplication':
        result =  num1*num2
    elif operation == 'division':
        result = num1/num2
    else:
        result = "Invalid opeartion"
    return result

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operation = input("Enter operation: ")

result=calculator(num1,num2,operation)
print(result)
user_input=eval(input())
user_input2=eval(input())
new_list=[num for num in user_input if num not in user_input2]
print(new_list)
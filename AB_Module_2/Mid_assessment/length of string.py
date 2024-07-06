def length(inpt):
    count=0
    for str in user_input:
        count=count+1
    return count

user_input = input("Enter the string: ")
string_length=length(user_input)
print(string_length)

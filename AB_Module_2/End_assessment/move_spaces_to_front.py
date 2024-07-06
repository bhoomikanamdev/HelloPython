def without_white_space(user_input):
    new_output=[letter for letter in user_input if letter!=" " ]
    #print(new_output)
    with_white= len(user_input)-len(new_output)
    #print(with_white)
    final= " " * (with_white)
    #print (final)
    result= '"' + final + "".join(new_output) + '"'
    return result

user_input=input()
output=without_white_space(user_input)
print(str(output))
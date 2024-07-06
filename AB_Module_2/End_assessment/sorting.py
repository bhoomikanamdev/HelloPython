def sorted_statement(user_input):
    to_list=[word for word in user_input.split(",")]
    sorted_list=",".join(sorted(to_list))

    return sorted_list


user_input=input()
output=sorted_statement(user_input)
print(output)
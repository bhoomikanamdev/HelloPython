def even_index(user_string):
    output=[val for index,val in enumerate(user_string) if index%2 == 0]
    return "".join(output)

user_string=input()
result_string= even_index(user_string)
print(str(result_string))
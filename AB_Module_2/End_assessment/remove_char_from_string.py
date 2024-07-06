def remove_all_char(user_string,char_to_keep):
    final=[char for char in user_string if char == char_to_keep ]
    return "".join(final)


user_string=input()
char_to_keep=input()
output=remove_all_char(user_string,char_to_keep)
print(output)
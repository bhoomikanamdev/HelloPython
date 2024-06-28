def char_count(user_input):
    upper_char_count=0
    lower_char_count=0
    special_char_count=0
    numeric_char_count=0

    for char in user_input:
        if char >='A' and char <='Z':
            upper_char_count=upper_char_count+1
        elif char >= 'a' and char <= 'z':
            lower_char_count=lower_char_count+1
        elif char >= '1' and char <= '9':
            numeric_char_count=numeric_char_count+1
        else:
            special_char_count=special_char_count+1
    return upper_char_count,lower_char_count,numeric_char_count,special_char_count

user_input=input()
output=char_count(user_input)
print(output)
def string_exchange(user_input):
        new_char=user_input[-1]+user_input[1:-1]+user_input[0]
        return new_char

user_input=input()
print(string_exchange(user_input))
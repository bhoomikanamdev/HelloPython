def duplicate_removed(user_input):
    print(user_input)
    updated_word=[]

    #word_without_duplicate=[char for char in user_input if char not in updated_word ]
    for char in user_input:
        if char not in updated_word:
            updated_word.append(char)

    return "".join(updated_word)

user_input=input()
output=duplicate_removed(user_input)
print(output)
def final_sent(sentence,words_to_remove):
    new_sentence=[letter for letter in sentence if letter not in words_to_remove]
    """for letter in sentence:
        if letter in words_to_remove:
            print(letter)
            del letter
            #sentence.replace(letter,"")"""
    return "".join(new_sentence)

sentence=input()
words_to_remove=input()
output=final_sent(sentence,words_to_remove)
print(output)
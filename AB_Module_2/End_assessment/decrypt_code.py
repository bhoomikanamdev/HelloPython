def decrypt_msg(code,key):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_code=[]
    for letter in code:
        new_idx=alphabet.index(letter)
        updated_index=(new_idx+key)%26
        updated_letter=alphabet[updated_index]
        new_code.append(updated_letter)
    return new_code

code=input()
key=int(input())
final_msg=decrypt_msg(code,key)
print(final_msg)
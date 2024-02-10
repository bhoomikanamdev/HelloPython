'''def unique_name(word):
    items = [word.split('-')]
    items.sort()
    print("-".join(items))

name_input= input()
unique_name(name_input)'''

name_input=input()
items = name_input.split('-')
items.sort()
print("-".join(items))






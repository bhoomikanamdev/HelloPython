'''string = "hello world"
new_string = ""
for i in range(len(string)):
    if i % 2 == 0:
        new_string += string[i]

print(new_string)'''

string = "Hello, world"
index = string.find(",")
if index != -1:
    new_string = string[:index] + "!"
    print(new_string)
else:
    print(string)


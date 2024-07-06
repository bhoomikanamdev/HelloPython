'''Write a Python program to count the number of characters (character frequency) in a string.

Example 1:
Input:
google.com

Output:
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}'''


user_input = input()
case_sensitive=user_input.lower()
final= {char: case_sensitive.count(char) for char in case_sensitive}
print(final)


'''user_input = input()
case_sensitive=user_input.lower()
final_output={}
for char in case_sensitive:
    final_output[char]=0
print(final_output)
#print(final_output['h'])
#print(final_output.get('h'))
for char in case_sensitive:
    if final_output[char]>=0:
        final_output[char] = final_output[char]+1
print(final_output)'''
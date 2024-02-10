'''Write a Python program to find the indexes of all None items in a given list.

Example 1:
Input:
[1, None, 5, 4,None, 0, None, None]

Output:
[1, 4, 6, 7]'''

user_input=eval(input())
result = [number for number in range(len(user_input)) if user_input[number] is None]
print(result)
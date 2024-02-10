'''Write a Python program to create a list taking alternate elements from a given list. (Using list comprehension)

Example 1:
Input:
["red", "black", "white", "green", "orange"]

Output:
['red', 'white', 'orange']'''

user_input=eval(input())
result= [words for words in user_input [::2]]
print (result)
'''When we work on Data Science projects, we start with Data Cleaning i.e removing all rows where the features have NA/None values. This is done to achieve maximum accuracy from our prediction models. So, write a Python program to remove None value from a given list. (Using list comprehension)

Example 1:
Input:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

Output:
[12, 0, 23, -55, 234, 89, 0, 6, -12]'''


nums = eval(input())
updated_list= [num for num in nums if num is not None]
print (updated_list)


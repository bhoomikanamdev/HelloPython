'''Mr. Alberto wants to remove some numbers from the list of numbers to test his equation for numerical research. So, write a Python program to help him to remove all elements from a given list present in another list. (Using list comprehension)

Example 1:
Input:
[1,2,3,4,5,6,7,8,9,10]

[2,4,6,8]

Output:
[1, 3, 5, 7, 9, 10]'''


list1 = eval(input())
list2 = eval(input())
updated_list= [value for value in list1 if value not in list2]
print (updated_list)
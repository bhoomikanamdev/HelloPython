'''str1 = "Analytics Vidhya"
str2 = ""
for i in str1:
    str2 = i + str2
print("The original string is: ", str1)
print("The reversed string is: ", str2)'''

'''output = str1[::-1]
print(output)'''

'''import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.flip(arr1)
print(arr2_)'''

'''import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = arr1[::-1]
print(arr1.size)

print(arr2)'''



'''lst1 = ['W', 'a', 'w', 'b']
lst2 = ['e', ' ', 'riting', 'log']
str="bhoomika"
lst3 = [x + y for x, y in zip(lst1, lst2)]
print(lst3)
print(len(lst1))
print(len(str))'''

# This is a global variable
'''x = 10
def func():
    # This is a local variable
    x = 5
    print(x)
func()
print(x)'''

'''def sum(a,b):
    z=a+b
    return z

print(sum(3,4))'''

'''x=int(input())
y=int(input())
sum = lambda x,y:x+y if x
print(sum(x,y))'''

'''max= lambda x,y : x if x> y else y
print(max(5,6))'''

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
print(arr1[:,0])
print(arr1[:[0]])
n=int(input())
factorial = 1
while n > 1:
    factorial = factorial*(n)
    n = n-1
print(factorial)


input_string = input()
new_list=input_string.split(' ')
#print(new_list)
result_list=[]
for item in new_list:
  if len(item) in [2, 3, 5, 7, 11]:
   result_list.append(item)
   listToStr = ' '.join(map(str, result_list))
print(listToStr)

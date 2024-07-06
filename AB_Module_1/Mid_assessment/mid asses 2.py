
#my_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#my_list = eval(input())
#for i in range(0,len(my_list)+1):
#   if i == 0 or i == 4 or i == 5:
#   #del my_list[4:6]
#del my_list[0]
#print(my_list)

my_list = eval(input())
result_list=[]
for (i,a) in enumerate(my_list):
    if i not in (0,4,5):
        result_list.append(a)
print(result_list)
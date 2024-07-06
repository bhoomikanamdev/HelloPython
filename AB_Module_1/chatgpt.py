my_list = eval(input())
result_list=[]
for (i,a) in enumerate(my_list):
    if i not in (0,4,5):
        result_list.append(a)
print(result_list)
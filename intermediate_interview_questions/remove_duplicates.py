lst = [ 1,2,3,1,2,4,5,6,4,5,3,4,1,2,1]
#print(set(lst))

unique_list=[]
dupli=[]

for i in lst:
    if i not in unique_list:
        unique_list.append(i)
    elif i not in dupli :
        dupli.append(i)

print(dupli)

a = "naman"
#if in == in [: :-1]
print(a[::-1])
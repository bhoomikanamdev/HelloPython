#pizza = ['mushroom','peparoni','becon','paneer','cheese','belpeper']
#for i in range (0,len(pizza),2):
    #print(i,pizza[i])
my_list = [1, 2, 3, 4,5]
a=[]
for i in my_list:
    if i == 1:
      continue
    if i == 4:
      break
    a.append(i)
print(a)
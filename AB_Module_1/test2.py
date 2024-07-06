user_input = 1
user_list=[]
while user_input != 0:
    user_input = int(input())
    user_list.append(user_input)
#print(user_list)

sum_of_input=sum(user_list)
mean_of_input = (sum(user_list)/(len(user_list)-1))

print("Average and Sum of the above numbers are: "+ str(mean_of_input) +" "+ str(float(sum_of_input)))

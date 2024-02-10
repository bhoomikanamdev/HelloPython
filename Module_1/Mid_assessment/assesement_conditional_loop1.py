'''my_list=[1,2,3,4,5,6,7]
#for i in my_list:
print(sum(my_list))
my_num=7856
lis_num=str(my_num)
print('7568'.split(' '))'''

number1 = int(input())
input_length=len(str(number1))
#print(input_length)
count=0
while input_length>1:
    count=count+1
    sum=0
    for val in str(number1):
        sum = sum+int(val)
    number1=sum
    input_length=len(str(number1))
    print("Step-" + str(count) + " Sum: " + str(number1))
    #input_length=input_length-1



#whether a no is prime or not

'''input_number = int(input())
i=2
is_prime="No is Prime"
while i < (input_number/2):
    if input_number%i != 0:
        i=i+1
    else:
        is_prime="No is not prime"
        break
print(is_prime)'''


#Check whether the given no is prime or not (boolean output)

#function definition
def is_prime_num(input_number1):
    i = 2
    is_prime = True
    while i < (input_number1 / 2):
        if input_number1 % i == 0:
            s_prime = False
            break;
        else:
            i = i + 1
    return is_prime

#funtcion execution call
input_number1 = int(input())
#is_prime_num(input_number1)
print(is_prime_num(input_number1))



#print prime number from 0 to input value

result_list=[]
input_range=int(input())
for number in range(1,input_range):
    #is_prime_num(number)
    if is_prime_num(number) is True:
        result_list.append(number)
print(result_list)




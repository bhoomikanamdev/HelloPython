def is_prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

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

input_string = input()
new_list=input_string.split(' ')
result_list=[]
for word in new_list:
    #print(word, len(word))
    if is_prime_num(len(word)) is True:
        result_list.append(word)
listToStr = ' '.join(map(str, result_list))
print(listToStr)
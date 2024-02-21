def remove_char(input_from_user,n):
    output1=input_from_user[n+1:]
    output2=input_from_user[:n]
    output=output2+output1
    return output

input_from_user = input()
n = int(input())
result=remove_char(input_from_user,n)
print(result)

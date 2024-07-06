start_number=int(input())
end_number = int(input())
digit_to_count=int(input())
count=0
for num in range(start_number,end_number+1):
    num_str= str(num)
    for digit in num_str:
        if int(digit) == digit_to_count:
            count = count + 1
#while len(str(num))<len(str(end_number))+1:
            #count=count+1
print(count)
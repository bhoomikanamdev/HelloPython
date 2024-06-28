nth = int(input())
n1,n2= 0,1
count = 0

if nth < 0 :
    print("please enter positive number")
elif nth == 1 :
    print("1")
else :
    print("fibonaccinis")
    while count < nth:
        print(n1)
        new = n1+n2
        n1=n2
        n2 = new
        count = count + 1

'''nterms = int(input("How many terms? "))
# 7
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8'''

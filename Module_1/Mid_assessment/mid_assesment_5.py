a=int(input())
b=int(input())
c=int(input())
if a == b == c:
    print("Equilateral triangle")
elif (a == b) or (a == c) or (b == c):
    print("Isosceles triangle")
else:
    print("Scalene triangle")

x = int(input())
y = int(input())
z = int(input())

if x == y == z:
        print("Equilateral triangle")
elif x==y or y==z or z==x:
        print("Isosceles triangle")
else:
        print("Scalene triangle")

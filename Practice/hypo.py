import math
def hypothenuis(a,b):
    c = round(math.sqrt((a*a) + (b*b)))
    return c


a = int(input())
b = int(input())
output = hypothenuis(a,b)
print(output)
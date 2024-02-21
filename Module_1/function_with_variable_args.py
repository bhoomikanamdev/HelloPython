
''''#function definition
def add(*args):
    print(args)
    print(len(args))
    sum = args[0]+args[1]+args[2]
    return sum

#func call
print(add(5,7,8))'''


#function definition
def add(*args):
    print(len(args))
    sum =0
    for index in range(len(args)):
        sum = sum + args[index]
    return sum

#func call
print(add(5,7))
print(add(5,7,8,5,4))
print(add(5,7,8,5,4,8,0,2))

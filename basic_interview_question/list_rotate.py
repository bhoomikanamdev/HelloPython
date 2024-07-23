def list_rotate(lst,n):
    # exit case
    if len(lst) == 0 or len(lst) == 1:
        return lst
    n = n % len(lst)
    def new_lst(lst,n):
        #base case
        if n == 0:
            return lst
        #recursive case
        else:
            return [lst[-1]] + new_lst(lst[:-1], n-1)
    return new_lst(lst,n)

lst = [1,2,3,4,5,6,7]
n = 3
output = list_rotate(lst,n)
print(output)
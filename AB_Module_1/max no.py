def find_max(list_by_user):
    max_num = 0
    for num in list_by_user:
        if num > max_num:
            max_num = num
    return max_num

list_by_user=eval(input())
print(find_max(list_by_user))
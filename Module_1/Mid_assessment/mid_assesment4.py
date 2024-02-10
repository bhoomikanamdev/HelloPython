input_list=eval(input())
input_num=int(input())

'''if min(input_list) < input_num:
  print("False")
else:
  print("True")'''

for (idx,val) in enumerate(input_list):
  if val < input_num:
    print("False")
    break
  elif idx==len(input_list)-1:
    print("True")
  else:
    continue


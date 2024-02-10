'''Sum odd Numbers ➖
In this activity, you will create a custom function in Python that takes a list of integers as an argument and returns the sum of all odd numbers in the list.'''

def sum_odd(lst):
  result=0
  for number in lst:
    if number%2 != 0:
      result = result+ number
  return result
lst=eval(input())

final_result = sum_odd(lst)
print(final_result)
def find_max(x,y,z):
  result=0
  if x>y:
    max_xy=x
  else:
    max_xy=y
  if max_xy>z:
    result=max_xy
  else:
      result=z

  return result

x = int(input())
y = int(input())
z = int(input())

print(find_max(x,y,z))

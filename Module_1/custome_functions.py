
def greet_user(username):
 """Display a simple greeting."""
 print("Hello!" + username)
greet_user("bhoomika")

def make_pizza(topping='bacon'):
 """Make a single-topping pizza."""
 print("Have a " + topping + " pizza!")
make_pizza()
make_pizza('pepperoni')


def printMin(a, b):
 if a > b:
  print(b, 'is minimum')
 elif a == b:
  print(a, 'is equal to', b)
 else:
  print(a, 'is minimum')


printMin(3, 4)
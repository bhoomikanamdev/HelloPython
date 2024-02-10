
import random
# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
print(secret_number)
# Write code here
no_of_tries = 1
max_try=3

while no_of_tries <=  max_try:
  user_input = int(input("Enter your number : "))
  if user_input == secret_number:
    print("you won")
    break
  elif no_of_tries==max_try:
      print("oopss! You exausted the limit ..The secret number is : " + str(secret_number))
  elif user_input < secret_number:
    print("your guess is lower than secret number")
  elif user_input > secret_number:
    print("your guess is more than secret number")
  no_of_tries=no_of_tries+1

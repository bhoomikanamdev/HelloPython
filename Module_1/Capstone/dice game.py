import random
random_dice_output= random.randint(1, 6)
def roll_dice(random_dice_output):
  return random_dice_output
output = roll_dice(random_dice_output)
print("The randon dice number is : " + str(output))

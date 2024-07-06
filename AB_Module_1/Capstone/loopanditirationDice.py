player_rolls = [
    [3, 5, 6, 2, 1],  # player 1's rolls
    [4, 4, 6, 3, 2],  # player 2's rolls
    [1, 5, 6, 6, 4]   # player 3's rolls
] # list of a list

max_avg = 0
max_player_index = 0
for index in range(len(player_rolls)):
  print(player_rolls[index])
  average_index = sum(player_rolls[index])/len(player_rolls[index])
  print(average_index)
  if average_index > max_avg:
    max_avg = average_index
    max_player_index= index
    #print(max_avg,max_player_index)
print("The max average is " + str(max_avg) + " by " + str(max_player_index+1))
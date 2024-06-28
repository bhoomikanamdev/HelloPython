def smiley_pyramid(rows):
   smiley = "😊"
   for i in range(1, rows + 1):
      # Print spaces for alignment
      print(' ' * (rows - i), end='')
      # Print smileys
      print(smiley * i)


# Example usage:
smiley_pyramid(5)

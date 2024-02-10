# Take input from the user
string = input("Enter a string: ")

# Initialize a count variable to 0
count = 0

# Loop through each character in the string
for char in string:
    # Check if the character is a vowel
    if char in "aeiouAEIOU":
        # If it is, increment the count
        count += 1

# Print the count of vowels
print("The number of vowels in the string is:", count)
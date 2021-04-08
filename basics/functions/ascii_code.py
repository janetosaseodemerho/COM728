# Display a start message
print("Program started")

# Prompt user to enter a standard character
print("Please enter a standard character:")
char = input()

# Check that a single letter has been entered
num_char = len(char)

if num_char == 1:
    # Determine the ASCII code of the character
    ASCII_code = ord(char)
    print(f"The ASCII code for {char} is {ASCII_code}.")
else:
    print("Invalid")

print("Program Ended!")

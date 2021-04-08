# displaying the start message
print("Program Started!")
print("Please enter an ASCII code:")
ASCII_code = int(input())
if ASCII_code in range(32, 127, 1):
    ASCII_character = chr(ASCII_code)
    print(f"The character represented by the ASCII code {ASCII_code} is {ASCII_character}.")
else:
    print("Invalid Entry")

print("Program Ended!")

# Prompt the user to enter a whole number
print("Please enter an whole number.")
number = int(input(""))

# Define the type of whole number
if number % 2 == 0:
    print(f"\nThe number {number} is an even number.")
else:
    print(f"\nThe number {number} is an odd number.")
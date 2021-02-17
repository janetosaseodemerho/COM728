# Ask the user to enter three numbers (one number at a time)
print("Please enter the first number.")
first_number = int(input())

print("\nPlease enter the second number.")
second_number = int(input())

print("\nPlease enter the third number.")
third_number = int(input())

# Determine how many of them are even or odd
even_number = 0
odd_number = 0

if first_number % 2 == 0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if second_number % 2 == 0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if third_number % 2 == 0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1

# Display the number of even numbers and odd numbers entered
print(f"\nThere were {even_number} even and {odd_number} odd numbers.")
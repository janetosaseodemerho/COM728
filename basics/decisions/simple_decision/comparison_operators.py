# Prompt the user to enter the first number
print("Please enter the first number.")
first_number = int(input())

# Prompt the user to enter the second number
print("\nPlease enter the second number.")
second_number = int(input())

# Then determine the comparison between the two numbers
if first_number < second_number:
    print("\nThe first number is the smallest!")
elif first_number > second_number:
    print("\nThe second number is the smallest!")
else:
    print("\nBoth are equal!")
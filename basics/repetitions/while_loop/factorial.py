# Ask user for a number
print("Please enter a number?")
number = int(input())

# Calculate factorial of the specified number
count = 0
total = 1

while count < number:
    count = count + 1
    total = total * count

print(f"\nThe factorial is {total}.")
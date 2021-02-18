# Ask user for number
print("How many numbers should I sum up?")
number = int(input())

print()
summed = 0
total = 0

while summed < number:
    print(f"Please enter number {summed} of {number}:")
    response = int(input())
    total = total + response
    summed = summed + 1

# Display result
print(f"\nThe answer is {total}.")
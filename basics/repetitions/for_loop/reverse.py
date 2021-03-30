print("What phrase do you see?")
user_phrase = input()

print("\nReversing...")
print("The phrase is ", end="")

for position in range(len(user_phrase)-1, -1, -1):
    print(user_phrase[position], end="")

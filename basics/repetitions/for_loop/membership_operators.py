print("What phrase do you see?")
user_phrase = input()

print("\nReversing...\n")
print("The phrase is ", end="")
Reversed = ""
for letters in user_phrase:
    Reversed = letters + Reversed

print(Reversed)

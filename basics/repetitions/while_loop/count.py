# Display the message
print("How many live cables must I avoid?")
numb_cables = int(input())
removed_cable = 0
print()
while removed_cable < numb_cables:
    print("Avoiding...", end="")
    removed_cable += 1
    print(f"Done! {removed_cable} live cables avoided.")

# finally display message
print("\nAll live cables have been avoided.")

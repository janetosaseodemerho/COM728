# Display the message
print("How many live cables must I avoid?")
numb_cables = int(input())
removed_cable = 0
print()
while removed_cable < numb_cables:
    print(f"Avoiding...Done! {removed_cable + 1} live cables avoided.")
    removed_cable += 1

# finally display message
print("\nAll live cables have been avoided.")
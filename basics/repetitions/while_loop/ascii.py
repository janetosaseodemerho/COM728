# Displaying the message
print("How many bars should be charged?")
numb_bars = int(input())

# Create a variable to track the number of bars charged
bars_charged = 0
while bars_charged < numb_bars:
    bars_charged += 1
    print(f"Charging:{' █'* bars_charged}")

# Finally, the program should display the message
print("\nThe battery is fully charged.")
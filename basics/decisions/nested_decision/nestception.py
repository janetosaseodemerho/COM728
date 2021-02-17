# Display message
print("Where should I look?")
direction = input()

if direction == "in the bedroom":
    print("\nWhere in the bedroom should I look?")
    bedroom_direction = input()
    if bedroom_direction == "under the bed":
        print("\nFound some shoes but no battery")
    else:
        print("\nFound some mess but no battery.")

elif direction == "in the bathroom":
    print("\nWhere in the bathroom should I look?")
    bedroom_direction = input()
    if bedroom_direction == "in the bathtub":
        print("\nFound a rubber duck but no battery")
    else:
        print("\nFound a wet surface but no battery.")

elif direction == "in the lab":
    print("\nWhere in the lab should I look")
    bedroom_direction = input()
    if bedroom_direction == "on the table":
        print("\nYes! I found my battery!")
    else:
        print("\nFound some tools but no battery.")

else:
    print("\nI do not know where that is but I will keep looking.")
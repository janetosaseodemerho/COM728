# Prompt the user for a direction to move the paint brush (up, down, left or right)
print("Towards which direction should I paint (up, down, left or right)?")
direction_type = input("")
print()
if direction_type == "up":
    print("I am painting in the upward direction!")
elif direction_type == "down":
    print("I am painting in the downward direction!")
elif direction_type == "left":
    print("I am painting in the left direction!")
elif direction_type == "right":
    print("I am painting in the right direction!")
else:
    print("Direction undefined")

# Ask the user to determine the cover type (hard or soft) of the book.
print("What type of cover does the book have?")
cover_type = input()
if cover_type == "soft":
    print("\nIs the book perfect-bound?")
    response = input()
    if response == "yes":
        print("\nSoft cover, perfect bound books are very popular!")
    else:
        print("\nSoft covers with coils or stitches are great for short books")
else:
    print("\nBooks with hard covers can be more expensive!")
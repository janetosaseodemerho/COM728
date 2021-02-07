print("")
# Ask user for a brief introduction
introduction = input("Please briefly introduce yourself:")
print("\nIt's nice to meet you.")
print()
# Ask user for description of an ASCII robot's features
eye = input("Please enter the character of ASCII robot's eyes:")
hand = int(input("Please enter the length of the hands:"))
print()
# Display beep's look
print("The ASCII robot's expression is now as follows:")
print()
print("\t \t \t  -######-")
print(f"\t \t    &/  {eye}  {eye}  \&")
print("\t \t     \  <-->  /")
print("\t \t \t   ------")
print(f"(?){'#'*hand}##########{'#'*hand}(?)")
print("\t \t    #          #")
print("\t \t   #        Beep#")
print("\t \t  #              #")
print("\t \t #                #")
print("\t \t ##################")
print("\t \t     (__/   \__)")
print()
# Ask user for ASCII robot's name
name = input("What is your ASCII robot's name?")
# Ask user for ASCII robot's height
height = float(input("How tall is it (in centimetres)?"))

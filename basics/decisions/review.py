# Ask user a question
print("Do you know the countries identified as permanent members of the United Nation security council?")
answer = input()
if answer == "yes":
    print("\nCan you mention one of the countries?")
    response = input()
    if (response == "Russia") or (response == "China") or (response == "France") or (response == "United Kingdom") or (response == "United States"):
        print("\nThat's correct!")
    elif (response == "russia") or (response == "china") or (response == "france") or (response == "united kingdom") or (response == "united states"):
        print("\nThat's correct!")
    elif (response == "Estonia") or (response == "India") or (response == "Ireland") or (response == "Saint Vincent") or (response == "Mexico") or (response == "Niger") or (response == "Norway") or (response == "Grenadines") or (response == "Tunisia") or (response == "Vietnam"):
        print("\nThis is a non-permanent member.")
    elif (response == "estonia") or (response == "india") or (response == "ireland") or (response == "saint vincent") or (response == "mexico") or (response == "niger") or (response == "norway") or (response == "grenadines") or (response == "tunisia") or (response == "vietnam"):
        print("\nThis is a non-permanent member.")
    else:
        print("\nThat's incorrect!")
else:
    print("\nThat's alright!")
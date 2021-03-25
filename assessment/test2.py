# The function should be named gang and should have no parameters.
def gang():
    # The function should start by displaying the message "Loading gang...".
    print("Loading gang...")
    # The function should then create a list named friends.
    # The function should then populate the list with the following values:
    friends = ['Scooby Doo', 'Shaggy Rogers', 'Fred Jones', 'Daphne Blake', 'Velma Dinkley']
    # The function should then display the list.
    print(friends)
    # The function should then display the message "...Done!".
    print("...Done!")
    # Finally, the function should return the list.
    return friends


def phrases(friends):
    # The function should start by creating a dictionary named quotes.
    quotes = {}
    # For each friend in the list friends, the function should do the following:
    # Display the message "What does {friend} say?" where {friend} is the name of the friend.
    for friend in friends:
        print(f"What does {friend} say?")
        # Read in the user's response and store it in a variable named quote.
        quote = input()
        # Add the value assigned to quote to the dictionary quotes using the friend's name as a key.
        quotes[f"{friend}"] = quote
    # Finally, the function should return the dictionary quotes.
    return quotes


# The function should be named save.
# The function should have 1 parameter named quotes which represents a dictionary of phrases
def save(quotes):
    # The function should start by opening the file "quotes.txt" in write mode.
    with open("quotes.txt", "w") as file:
        # For each item in the dictionary quotes, the function should do the following:
        for friend, quote in quotes.items():
            # Write the item to the file on a new line
            file.write(f"{friend}: {quote}\n")


def run():
    friends = gang()
    quotes = phrases(friends)
    print(f"\nPhrases: {quotes}\n")
    save(quotes)
    print("The file contains...")
    file = open("quotes.txt")
    print(file.read())
    file.close()


run()

# Ask user for number of mountains
print("How many mountains should I display?")
mountains = int(input())

# Then display mountains
print("\nDisplaying...")

for mountain in range(mountains):
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\

  """)

# finally
print("\nDone!")
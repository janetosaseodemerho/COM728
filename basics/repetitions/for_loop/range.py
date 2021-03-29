print("What level of brightness is required?")
response = int(input())

for brightness in range(2, response+1, 2):
    print("\nAdjusting brightness...")
    print(f"\nBeep's brightness level: {'*'* response}")
    print(f"Bop's brightness level: {'*'* response}")

print("\nAdjustments complete!")

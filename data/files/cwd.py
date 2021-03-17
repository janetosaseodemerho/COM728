# Display information about the current working directory
import os

# Retrieve the file path and display each file contained in the current working folder
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)

def run():
    print("Processing...")
    cwd()

run()
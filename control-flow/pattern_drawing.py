# This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*)
size = int(input("Enter the size of the pattern:"))

# Ensure it's a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

# Get user input as string
num_str = input("Enter a number: ")

# Convert input to integer and check if it's positive, negative, or zero
num = int(num_str)
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
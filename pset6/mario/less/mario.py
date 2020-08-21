# Import cs50 Library
from cs50 import get_int

# Get input
height = get_int("Height: ")

# Get only values between 1 and 8
while True:
    if height > 0 and height < 9:
        break
    else:
        # Ask againg until correct input
        height = get_int("Height: ")

# Print the pyramid
for x in range(height):
    j = x + 1
    print(" " * (height-j), end="")
    print("#" * j, end="")
    print()
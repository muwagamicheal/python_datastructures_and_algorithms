# here we shall be using regular expressions to determine if the number is even or odd.

import re

def is_even(k):
    binary_representation = bin(k)[2:]  # Convert to binary and remove '0b' prefix
    return bool(re.match(r'^.*0$', binary_representation))

# Capture user input
number = input("Enter an interger \n")
# pass it to the function and store the result in the varialble result.
result = is_even(number)
# Display the number entered by the user and the result.
print(f"{number} is even: {result}")

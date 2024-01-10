# here we shall be using regular expressions to determine if the number is even or odd.

import re

def is_even(k):
    binary_representation = bin(k)[2:]  # Convert to binary and remove '0b' prefix
    return bool(re.match(r'^.*0$', binary_representation))

# Test the function
number = int(input("Enter an interger \n"))
result = is_even(number)
print(f"{number} is even: {result}")

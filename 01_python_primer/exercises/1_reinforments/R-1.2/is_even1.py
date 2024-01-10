# Here we are using the bitwise operator to check if the number is even or odd

def is_even(k):
    return k & 1 == 0

# Test the function
number = 19
result = is_even(number)
print(f"{number} is even: {result}") # here is use the f-string to pass varialble to the output.

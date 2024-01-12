import re

def is_even(m):
  """
  # Option 1
  result = bool(re.match(r'.*[02468]$',str(m)))
  return result"
  """
  # Option 2
  if re.search(r"\d*[02468]$", str(m)):
    return True
  else:
    return False
  

# Capture user input
number = int(input("Enter an interger \n"))
# Pass it to the function and store the result in the varialble result.
result = is_even(number)
# Display the number entered by the user and the result.
print(f"{number} is even: {result}")

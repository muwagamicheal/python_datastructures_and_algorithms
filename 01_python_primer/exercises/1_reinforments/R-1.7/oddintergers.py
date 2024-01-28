
def oddintegers():
  # Capturing user input
  n = int(input("Enter a postive integer greater than 2\nI will  return the sum of all squares lessthan n \n"))
  # Single command as required in the assignment.
  s = sum([x**2 for x in range(n) if (x%2 == 1) ])
  print(s)
  return s
oddintegers()
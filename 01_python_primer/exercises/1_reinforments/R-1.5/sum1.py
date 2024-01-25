
def user_input():
  # Capturing user input
  n = int(input("Enter a postive integer greater than 2\nI will  return the sum of all squares lessthan n \n"))

  # Using list comprehension to generate a list of squares lessthan n.
  squares = [x**2 for x in range(n) if n >= 0 ]
  
  # Out put the list of squares
  print(squares)

  # Using the inbulit sum() function
  s = sum(squares)
  print(s)
  return s
user_input()
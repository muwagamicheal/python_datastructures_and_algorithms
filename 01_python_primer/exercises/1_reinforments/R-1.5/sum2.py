
def user_input():
  # Capturing user input
  n = int(input("Enter a postive integer greater than 2\nI will  return the sum of all squares lessthan n \n"))

  # Single command
  s = sum([x**2 for x in range(n) if n>= 0])
  #print the results to the screen
  print(s)
  return s # return sum.
user_input()
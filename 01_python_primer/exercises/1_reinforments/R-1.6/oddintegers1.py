
def oddintegers():
  # Capturing user input
  n = int(input("Enter a postive integer greater than 2\nI will  return the sum of all squares lessthan n \n"))
  """
  # List of odd postive integers method 1
  oddm1 = [x for x in range(n) if x%2 == 1]
  print(oddm1)

  # List of odd postive integers method 2
  oddm2 = [x for x in range(n) if x%2 != 0 ]
  print(oddm2)
  
  # List of even postives
  # even = [x for x in range(n) if x%2 == 0 ]
  # print(even)
  """
  # Using list comprehension to generate a list of squares lessthan n.

  squares = [x**2 for x in range(n) if (x%2 == 1) ]
  
  
  # Out put the list of squares
  print(squares)

  # Using the inbulit sum() function
  s = sum(squares)
  print(s)
  
  return s
oddintegers()
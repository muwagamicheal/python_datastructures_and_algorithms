from math import sqrt

def squares (n):
  # This function calculates and returns the sum of all numbers less than n.
  sum = 0
  for index in range (1, n):
    #sum = sum + (index * index) # basic way of implementing squares
    sum += index**2 # this is better that the line above
  print(f"Your input:{n}, the sum:{sum}") # show the sum before returning it.
  return sum

def get_input():
  m = 0
  #Check if the user input is postive
  while m <= 0:
    #Turn user input to integer
    m = int(input("Enter a postive integer greater than 2\nI will  return the sum of all squares lessthan n \n"))
    
  return m

# Passing the getinput() function to the squares()
user_input = get_input()
n = user_input
squares(n)

"""
random.randrange(stop)
random.randrange(start, stop[, step])
  Return a randomly selected element from range(start, stop, step). This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
""" 
from random import randrange
#generate random number in the range of -100 to 100.
n = randrange(-10000000,10000000)
print(n)

#If you want to generate 5 random values and save in list.
# The code below is not part of the assignment.
lst = []
for x in range(5):
  n = randrange(-100,100)
  lst.append(n)
print(lst)
"""
random.randrange(stop)
random.randrange(start, stop[, step])
  Return a randomly selected element from range(start, stop, step). This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
""" 
from random import randrange

# pick anumber form a squence using randrange
import random

def my_choice(data):
    if not data:
        raise ValueError("Sequence must be non-empty.")

    # Use randrange to generate a random index within the range of the sequence
    random_index = random.randrange(len(data))

    # Return the element at the randomly chosen index
    return data[random_index]

# Example usage:
my_list = [1, 2, 3, 4, 5]
random_element = my_choice(my_list)
print("Randomly chosen element:", random_element)


#generate random number in the range of -100 to 100.
n = randrange(-100,100)
print(n)

# 

#If you want to generate 5 random values and save in list.
# The code below is not part of the assignment.
lst = []
for x in range(5):
  n = randrange(-100,100)
  lst.append(n)
print(lst)

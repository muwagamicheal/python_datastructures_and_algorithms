# imports
from random import randrange #Import randrange function from the random module.

def generateSequence ():
    #generates the sequence.
    sqn = []
    for n in range(15):
        n = randrange(-999,999)
        sqn.append(n)
    return sqn

sequence = generateSequence()
print(sequence)


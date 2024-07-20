# imports
from random import randrange #Import randrange function from the random module.

def generateSequence ():
    #generates the sequence.
    sqn = []
    for n in range(15):
        n = randrange(-999,999)
        sqn.append(n)
    return sqn

def oddProduct(sequence):
    for p in range(len(sequence)-1):
        #product = sequence[p]*(sequence[p+1])
        value1 = sequence[p]
        value2 = sequence[p+1]
        p1 =[p]
        p2 =[p+1]
        product = value1*value2
        print(product)
        
        if product%2 != 0:
            print(f"odd pair found by multiplying values {value1} and {value2} at {p1} and {p2} in the sequence below")
            #print("Odd pair found")
            break
        else:
            print("Looking for odd pair")
            print("Did not find odd pair")
    return print

sequence = generateSequence()
oddProduct(sequence)
print(sequence)

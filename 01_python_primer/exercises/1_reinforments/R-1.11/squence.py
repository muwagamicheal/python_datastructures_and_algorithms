# Setting paramters
start = 0
stop  = 9
step  = 1
#x = x + x**2
sequence =[ 2**x for x in range(start,stop, step)] # using list comprehension to generate the sequence.
print(sequence)
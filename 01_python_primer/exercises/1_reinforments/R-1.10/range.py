# how to use range with all parameters supplied

start = 8
stop = -9 # try setting -9 as the stop value  and check the output of sequence.
step = -2
# all parameters supplied
sequence =[x for x in range(start,stop, step)] # using list comprehension to generate the sequence.
print(sequence)
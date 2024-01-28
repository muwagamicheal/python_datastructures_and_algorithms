# how to use range
#all parameters supplied

start = 50
stop = 85 # try setting any number between 81 and 100 and check the output of sequence1.
step = 10
# all parameters supplied
sequence1 =[x for x in range(start,stop, step)] # using list comprehension to generate the sequence.
print(sequence1)
# the exmples below are for clafication and are not par of the assignment.
# step parameter not supplied
sequence2 = [ x for x in range(start,stop)] 
print(sequence2)

# stop parameter not supplied.
sequence3 = [x for x in range(start, step)]
print(sequence3)

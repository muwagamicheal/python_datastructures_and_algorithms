# imports
from random import randrange #Import randrange function from the random module.

# generating a list using randrange
sqn1 = []
for x in range(15):
  n = randrange(-100,100)
  sqn1.append(n)
print(sqn1)

def reverse(sqn1):
  ''' reverses a list '''
  rev_sqn1 = []
  for x in range(len(sqn1)-1,-1,-1):
    rev_sqn1.append(sqn1[x])
  return rev_sqn1

reversed_list = reverse(sqn1)
print(f'The original list:\n{sqn1}') # Using fstring to display test and variables.
print(f'The reversed list:\n{reversed_list}')

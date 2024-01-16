# Using conditional loops
'''
In this approach we use the while loop to iterate over the sequence, and the if loops are used to compare the number in the list with one thats stored in the nmin or nmax variable. If the number in the list in lower of greater that the one stored, the stored varialbe will be replaced. This will continue until the loops have iterated over the full length in the squence. Then the result stored in the min and max varialbles will be returned as a tuple.
'''

# Capture user input and store it in a list named sequence.
def get_input():
  sequence = []
  while True:
    var = input("Enter a number I will add it to the seqeunce to be checked.\n'#' I will start checking.\n") 
    '''
    if checker == int:
      #userIn = checker
      sequence.append(checker)
    if checker =='#':
      print("Let me Check  the Sequence")
      break
    '''
    if var =='#':
      break
    try:
      sequence.append(float(var))
    except ValueError:
      print("Invalid input")
  
  print(sequence)
  return sequence
# Checking for the max and min values using conditional loops.
def minmax(user_input):
  nmin = user_input[1]
  nmax = user_input[1]
  # nmin = nmax = user_input[1] #the code on the left works as the two lines above.
  index = 1
  while(index < len(user_input)):    
    if user_input[index] < nmin:
      nmin = user_input[index]
    if user_input[index] >  nmax:
      nmax = user_input[index]
    index += 1
  results = (nmin,nmax)
  print(f"the minimun number is:{nmin}\nthe maximun number is:{nmax}\nThe tuple is on the next line\n{results}")
  return results

sequence = get_input()
user_input = sequence
minmax(user_input)
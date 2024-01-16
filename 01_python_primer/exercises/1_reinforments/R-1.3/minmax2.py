# Using the built in sort method.

# Get user input
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

def minmax(user_input):
  # Using sort() list method
  user_input.sort()
  print(user_input)
  nmin = user_input[0]
  nmax = user_input[-1]

  results = (nmin,nmax)
  print(f"the minimun number is:{nmin}\nthe maximun number is:{nmax}\nThe tuple is on the next line\n{results}")
  return results

sequence = get_input()
user_input = sequence
minmax(user_input)
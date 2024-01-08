
# In this solution we create alist of mulptiples of a given number.
def is_multiple(n,m):
  item = 1
  multiples = []
  #creating multiple of the given number
  for item in range(1,m+1):
    if m % item == 0:
      multiples.append(item)
    item += 1
  print(multiples)

  # Checking if the number is a multiple
  if m%n == 0:
    print(True)
  else:
    print(False, )

is_multiple(2,150) 

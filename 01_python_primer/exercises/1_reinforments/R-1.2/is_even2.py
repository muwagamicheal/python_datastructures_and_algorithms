#Using conditional loops
number = int(input("Enter an integer, I will tell you if its even or Not"))
while(number >= 2):
  number = number -2
if number == 0:
  print(True,"The number is Even")
else:
  print(False,"The number is odd")

# Future Improvments 
  " Include error handling when the user  enters numbers with decimals or charcters "
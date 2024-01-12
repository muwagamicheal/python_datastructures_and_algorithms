## Assignment
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.

## Solution(s)
### 1. Using conditional loops
In this approach we use the while loop to compare the number in the list with one thats stored in the min or max variable. If the number in the list in lower of grater that the one stored, the stored varialbe will be replaced. This will continue the loops have iterated over the full length in the squence.
### 2. Using the sort function
In this appproach we shall use sort the sequence then return the first number in the sequence as the min, and rturn the last number in the squecence as the max.

# Improvments:
  The solution files contain the simplest implimentations, you can extend them as need.
  
  1. You can Include error handling when the user  enters numbers with decimals or charcters.

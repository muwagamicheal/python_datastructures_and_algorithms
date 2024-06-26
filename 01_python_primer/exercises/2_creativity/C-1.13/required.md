## Assignment
Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.

### Solution(s)
## Using negative indexing
By default a sequence is created and indexed starting from 0 up to the length of the sequence n.
To reverse this sequence i will use a for loop and range function to iterated on the list in reverse order.
## Pseudo-code

    function reverse(sqn1):
        # Create an empty list to store the reversed elements
        rev_sqn1 = []

        # Iterate through the original list in reverse order
        for i = length(sqn1) - 1 to 0 step -1:
            # Append the current element to the reversed list
            append(rev_sqn1, sqn[i])

        # Return the reversed list
        return rev_sqn1

Explanation:

Function definition:

reverse(sqn1): Defines a function named reverse_list that takes a list as input.
Initialization:

rev_sqn1 = []: Creates an empty list to store the reversed elements.
Looping through the list:

for i = length(sqn1) - 1 to 0 step -1: Iterates from the last index of the list to the first index, decrementing by 1 in each step.
Reversing elements:

append(rev_sqn1, sqn[i]): Appends the current element at index i of the original list to the reversed_list. This effectively reverses the order of elements.
Returning the reversed list:

return rev_sqn1: Returns the created reversed_list containing the elements in reversed order.
s = "abcdefgh"
n = len(s)

# Using negative index k
k = -3
equivalent_index = n + k

# Accessing the element at index k
element_at_k = s[k]

# Accessing the equivalent element at index j
element_at_j = s[equivalent_index]

print(f"s[{k}] is equivalent to s[{equivalent_index}]: {element_at_k} == {element_at_j}")

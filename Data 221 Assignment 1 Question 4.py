# Tafheem Khan 30219735
# Data 221 Assignment_1 Question 4 "Sorted Search with Conditions"
# Need to be able to sort a list of random values between 1 and 0 and a random variable, need to sort said list find where it is bigger then the random variable, and finally print the sorted list, value of x and if a first matching index exists that as well
from random import random

values = [random() for i in range(20)]
x = random()

# Need something to sort the list
values.sort()

# Find all instances where the value >= x
indices = [i for i, v in enumerate(values) if v >= x]

# Print results
print("Sorted list:", values)
print("x:", x)
# print the first value where x is smaller or equal. print no values if x is bigger then all.
if indices:
    print("First matching index:", indices[0])
else:
    print("No values greater than or equal to x")

# Tafheem Khan 30219735
# Data 221 Assignment_1 Question 3 "Safe Function Application"
# need to first make a function that does x^y
def power(x, y):
    return x ** y
# then get a list of pairs of (x,y)
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
# now i need to use a for loop that will first neglect any pairs where y is negative, runs the values through my function and then puts them in a different list and prints said list

# final list
results = []
for x, y in pairs:
    # will pairs where the exponent is negative
    if y < 0:
        continue

    # will do the power function and add to my final list
    results.append(power(x, y))
# now need to print the list of valid results
print(results)
# Tafheem Khan 30219735
# Data 221 Assignment_1 Question 1 "Controlled Multiplication Loop"
# I need to make a code which will multiply consecutive integers from 1 onward
# the code also needs to store 3 values, the threshold value(WHERE THE loop needs to end) the product(the number which i will need to get as close to the threshold value) and the current number(the number i will be multiplying by)
#need to first identify the variables i will be using
Threshold_Value = 1402
Product = 1
Current_Multiplier = 1
# need the while loop to keep going until the product is greater then the threshold value
while Product <= Threshold_Value:
    Product = Product * Current_Multiplier
    Current_Multiplier += 1
    # need to store the threshold value in a variable (check)
    # Keep track of the current multiplier (check)
    # print the final product and the integer that caused the product to exceed the threshold (haven't done this yet)
    # need to subtract one from the current multiplier as it was added but never multiplied by that
print(f"The threshold of {Threshold_Value} was able to make it until {Product} which is the multiplier of {Current_Multiplier-1}")
#ok achieved the goal now
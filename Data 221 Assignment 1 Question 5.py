# Tafheem Khan 30219735
# Data 221 Assignment_1 Question 5 "Circle Area Comparison with Validation"
# Need to make a function that takes the radii of 2 circles and Validates both are positive integers, computes the area of each and returns the % of the larger one that can be covered by the smaller one
# need to not do a calculation if the input is invalid
import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # Need to validate the inputs, need to first confirm they are integers then need to check if they are also positive
    if (not isinstance(radiusOfCircle1, int) or
        not isinstance(radiusOfCircle2, int)):
        return "Both radii must be integers."

    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Both radii must be positive integers."

    # Need to now compute the areas of both circles
    AreaOfCircle1 = math.pi * radiusOfCircle1 ** 2
    AreaOfCircle2 = math.pi * radiusOfCircle2 ** 2

    # Find which one is smaller and larger
    SmallerAreaOfCircle = min(AreaOfCircle1, AreaOfCircle2)
    LargerAreaOfCircle = max(AreaOfCircle1, AreaOfCircle2)

    # Calculate the percentage coverage
    percentage = (SmallerAreaOfCircle / LargerAreaOfCircle) * 100
    # Return the percentage
    return percentage


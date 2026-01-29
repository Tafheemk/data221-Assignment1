# Tafheem Khan 30219735
# Data 221 Assignment_1 Question 8 "Pandas DataFrame with Computed Column"
#need to install panda(done) and import using pd(also done) and then, Create a dataframe using the data, add a new colum derived from exiting columns and print the final data frame
import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Create a DataFrame
DataFrame = pd.DataFrame(data)

# Add a new computed column
DataFrame["A_times_B"] = DataFrame["A"] * DataFrame["B"]

# Print final updated DataFrame
print(DataFrame)

import pandas as pd

# Define two matrices as lists of lists
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

# Convert the matrices to pandas DataFrames
df1 = pd.DataFrame(matrix1)
df2 = pd.DataFrame(matrix2)

# Perform matrix addition
result_addition = df1 + df2

# Perform matrix subtraction
result_subtraction = df1 - df2

# Perform matrix multiplication
result_multiplication = df1.dot(df2)

# Print the results
print("Matrix Addition:")
print(result_addition)
print("\nMatrix Subtraction:")
print(result_subtraction)
print("\nMatrix Multiplication:")
print(result_multiplication)

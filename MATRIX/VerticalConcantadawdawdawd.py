import numpy as np
rows1 = int(input("Enter the number of rows for matrix1: "))
cols1 = int(input("Enter the number of columns for matrix1: "))
matrix1 = np.zeros((rows1, cols1))
print("Enter the elements for matrix1:")
for i in range(rows1):
    for j in range(cols1):
        matrix1[i][j] = int(input(f"Enter element at position ({i+1}, {j+1}): "))
rows2 = int(input("Enter the number of rows for matrix2: "))
cols2 = int(input("Enter the number of columns for matrix2: "))
matrix2 = np.zeros((rows2, cols2))
print("Enter the elements for matrix2:")
for i in range(rows2):
    for j in range(cols2):
        matrix2[i][j] = int(input(f"Enter element at position ({i+1}, {j+1}): "))
result = np.vstack((matrix1, matrix2))
print(result)

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def main():
    m1 = int(input("Enter the number of rows in matrix 1: "))
    n1 = int(input("Enter the number of columns in matrix 1: "))
    matrix1 = []
    for i in range(m1):
        row = []
        for j in range(n1):
            element = int(input("Enter element ({}, {}): ".format(i+1, j+1)))
            row.append(element)
        matrix1.append(row)
    m2 = int(input("Enter the number of rows in matrix 2: "))
    n2 = int(input("Enter the number of columns in matrix 2: "))
    matrix2 = []
    for i in range(m2):
        row = []
        for j in range(n2):
            element = int(input("Enter element ({}, {}): ".format(i+1, j+1)))
            row.append(element)
        matrix2.append(row)
    result = multiply_matrices(matrix1, matrix2)
    print("Result:")
    print(result)

if __name__ == '__main__':
    main()

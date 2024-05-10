def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions"
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
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
    result = add_matrices(matrix1, matrix2)
    print("Result:")
    print(result)

if __name__ == '__main__':
    main()
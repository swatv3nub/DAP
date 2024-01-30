def get_kth_column(matrix, k):
    return [row[k] for row in matrix]

def main():
    n = int(input("Enter the number of rows in matrix: "))
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input("Enter element ({}, {}): ".format(i+1, j+1)))
            row.append(element)
        matrix.append(row)
    k = int(input("Enter the column number: "))
    result = get_kth_column(matrix, k)
    print("The {}th column of the matrix is: {}".format(k, result))

if __name__ == '__main__':
    main()
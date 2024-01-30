def trans(matrix):
    return [list(row) for row in zip(*matrix)]

def main():
    m1 = int(input("Enter the number of rows in matrix 1: "))
    n1 = int(input("Enter the number of columns in matrix 1: "))
    matrix = []
    for i in range(m1):
        row = []
        for j in range(n1):
            element = int(input("Enter element ({}, {}): ".format(i+1, j+1)))
            row.append(element)
        matrix.append(row)
    result =  trans(matrix)
    print("Transpose of Matrix:\n")
    for r in result:
        print(r)

if __name__ == '__main__':
    main()
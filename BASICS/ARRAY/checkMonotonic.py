def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) 
            or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        arr.append(element)
    result = isMonotonic(arr)
    print("Is Monotonic: ", result)
    
if __name__ == '__main__':
    main()
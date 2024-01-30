def calculate_sum(arr):
    return sum(arr)

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        arr.append(element)

    result = calculate_sum(arr)
    print("Sum of the array is:", result)

if __name__ == '__main__':
    main()
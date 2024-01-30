def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        arr.append(element)

    result = find_largest(arr)
    print("Largest element in the array is:", result)

if __name__ == '__main__':
    main()
def find_remainder(arr, n):
    mul = 1
    for i in arr:
        mul = (mul * (i % n)) % n
    return mul % n

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        arr.append(element)
    result = find_remainder(arr, n)
    print("Remainder of the array is:", result)

if __name__ == '__main__':
    main()
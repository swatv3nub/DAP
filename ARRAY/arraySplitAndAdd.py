def split_and_add(arr):
    length = len(arr)
    if length == 0:
        return arr
    mid = length // 2
    first_half = arr[:mid]
    second_half = arr[mid:]
    return second_half + first_half

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        arr.append(element)

    result = split_and_add(arr)
    print("Rotated array is:", result)

if __name__ == '__main__':
    main()
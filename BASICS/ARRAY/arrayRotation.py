def rotate_array(arr):
    if len(arr) == 0:
        return arr
    last_element = arr.pop()
    arr.insert(0, last_element)
    return arr

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        arr.append(element)

    result = rotate_array(arr)
    print("Rotated array is:", result)

if __name__ == '__main__':
    main()
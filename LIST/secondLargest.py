def secondLargest(lst):
    largest = lst[0]
    secondLargest = lst[0]
    for element in lst:
        if element > largest:
            secondLargest = largest
            largest = element
        elif element > secondLargest:
            secondLargest = element
    return secondLargest

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = secondLargest(lst)
    print("Second largest element in the list is:", result)

if __name__ == '__main__':
    main()
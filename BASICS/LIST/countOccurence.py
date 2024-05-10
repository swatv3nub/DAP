def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    element = int(input("Enter the element to count: "))
    result = count_occurrences(lst, element)
    print("Number of occurrences of {}: {}".format(element, result))

if __name__ == '__main__':
    main()
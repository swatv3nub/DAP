def largest(lst):
    largest = lst[0]
    for element in lst:
        if element > largest:
            largest = element
    return largest

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = largest(lst)
    print("Largest element in the list is:", result)

if __name__ == '__main__':
    main()
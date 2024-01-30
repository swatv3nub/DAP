def clone(lst):
    return lst[:]

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = clone(lst)
    print("Original list:", lst)
    print("Cloned list:", result)

if __name__ == '__main__': 
    main()
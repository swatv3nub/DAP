def remove_elements(lst, elements):
    return [x for x in lst if x not in elements]

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    elements = []
    m = int(input("Enter the number of elements to remove: "))
    for i in range(m):
        element = int(input("Enter element {}: ".format(i+1)))
        elements.append(element)
    result = remove_elements(lst, elements)
    print("List after removing elements:", result)

if __name__ == '__main__':  
    main()
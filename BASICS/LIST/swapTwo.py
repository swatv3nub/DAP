def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    index1 = int(input("Enter the first index: "))
    index2 = int(input("Enter the second index: "))
    swap_elements(lst, index1, index2)
    print("List after swapping elements:", lst)

if __name__ == '__main__':
    main()

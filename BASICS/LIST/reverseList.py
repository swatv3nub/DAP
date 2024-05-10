def rev_list(lst):
    lst = lst[::-1]
    return lst

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    lst = rev_list(lst)
    print("Reversed list:", lst)
    
if __name__ == '__main__':
    main()
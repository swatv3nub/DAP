def interchange_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = interchange_first_last(lst)
    print("Interchanged list is:", result)

if __name__ == '__main__':
    main()

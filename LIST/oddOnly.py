def odd(lst):
    odd = []
    for element in lst:
        if element % 2 != 0:
            odd.append(element)
    return odd

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = odd(lst)
    print("List of odd numbers:", result)

if __name__ == '__main__':
    main()
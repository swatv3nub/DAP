def even(lst):
    even = []
    for element in lst:
        if element % 2 == 0:
            even.append(element)
    return even

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = even(lst)
    print("List of even numbers:", result)

if __name__ == '__main__':
    main()
def print_duplicates(lst):
    duplicates = []
    for num in lst:
        if lst.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    for duplicate in duplicates:
        print(duplicate)

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    print("Duplicates in the list:")
    print_duplicates(lst)

if __name__ == '__main__':
    main()

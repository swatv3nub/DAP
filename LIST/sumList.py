def sumList(lst):
    sum = 0
    for element in lst:
        sum += element
    return sum

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = sumList(lst)
    print("Sum of the list is:", result)

if __name__ == '__main__':
    main()
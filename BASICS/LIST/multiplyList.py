def multList(lst):
    mult = 1
    for element in lst:
        mult *= element
    return mult

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = multList(lst)
    print("Multiplication of the list is:", result)

if __name__ == '__main__':
    main()
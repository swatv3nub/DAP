def negs(lst):
    return [i for i in lst if i < 0]

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = negs(lst)
    print("List of negative numbers:", result)
    
if __name__ == '__main__':
    main()
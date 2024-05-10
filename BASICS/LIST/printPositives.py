def positives(lst):
    return [i for i in lst if i > 0]

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = positives(lst)
    print("List of positive numbers:", result)
    
if __name__ == '__main__':
    main()
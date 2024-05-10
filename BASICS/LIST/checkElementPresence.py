def check_element_in_list(element, lst):
    return element in lst

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    element = int(input("Enter the element to be checked: "))
    result = check_element_in_list(element, lst)
    print(f"Is {element} present in the list: {result}")
    
if __name__ == '__main__':
    main()
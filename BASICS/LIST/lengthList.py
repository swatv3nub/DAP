
def length_list(lst):
    length = 0
    for element in lst:
        length += 1
    return length

def main():
    
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = length_list(lst)
    print("Length of the list is:", result)

if __name__ == "__main__":
    main()
import heapq

def n_largest(lst, n):
    return heapq.nlargest(n, lst)

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    n = int(input("Enter the value of n: "))
    result = n_largest(lst, n)
    print(f" The largest {n} element in the list is: {result}")
    
if __name__ == '__main__':  
    main()
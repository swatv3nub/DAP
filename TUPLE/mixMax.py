import heapq

def find_max_min_k_elements(tup, k):
    max_k = heapq.nlargest(k, tup)
    min_k = heapq.nsmallest(k, tup)
    return max_k, min_k

def main():
    user_input = input("Enter elements of the tuple: ")
    elements = map(int, user_input.split())
    my_tuple = tuple(elements)
    k = int(input("Enter the value of k: "))
    max_k, min_k = find_max_min_k_elements(my_tuple, k)
    print("Max k elements:", max_k)
    print("Min k elements:", min_k)

if __name__ == '__main__':
    main()
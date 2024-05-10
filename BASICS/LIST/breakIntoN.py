def break_into_chunks(lst, N):
    return [lst[i:i+N] for i in range(0, len(lst), N)]

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    N = int(input("Enter the value of N: "))
    result = break_into_chunks(lst, N)
    print("List after breaking into chunks of size {}:".format(N))
    print(result)

if __name__ == '__main__':
    main()
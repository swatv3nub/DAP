def cummmm(lst):
    cum_sum = 0
    result = []
    for num in lst:
        cum_sum += num
        result.append(cum_sum)
    return result

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    result = cummmm(lst)
    print("Cumulative sum of elements:", result)

if __name__ == '__main__':
    main()
def order_tuples(tuples, order):
    return sorted(tuples, key=lambda tup: order.index(tup[0]))

def main():
    n = int(input("Enter the number of tuples: "))
    tuples = []
    for _ in range(n):
        tup = tuple(input("Enter the elements of the tuple separated by space: ").split())
        tuples.append(tup)
    order = input("Enter the order list separated by space: ").split()
    ordered_tuples = order_tuples(tuples, order)
    print(ordered_tuples)

if __name__ == "__main__":
    main()
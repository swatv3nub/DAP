def flatten_tuple(t):
    flattened = tuple(item for sublist in t for item in sublist)
    return flattened

def main():
    n = int(input("Enter the number of sub-tuples: "))
    tuples = []
    for _ in range(n):
        tup = tuple(map(int, input("Enter the elements of the sub-tuple separated by space: ").split()))
        tuples.append(tup)
    flattened_tuple = flatten_tuple(tuples)
    print(flattened_tuple)

if __name__ == "__main__":
    main()
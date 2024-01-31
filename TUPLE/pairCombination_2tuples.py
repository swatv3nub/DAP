from itertools import product

def pair_combinations(tuple1, tuple2):
    return list(product(tuple1, tuple2))

def main():
    tuple1 = tuple(input("Enter the elements of the first tuple separated by space: ").split())
    tuple2 = tuple(input("Enter the elements of the second tuple separated by space: ").split())
    pairs = pair_combinations(tuple1, tuple2)
    print(pairs)

if __name__ == "__main__":
    main()
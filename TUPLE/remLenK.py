def remove_tuples_of_length(tuples, k):
    return [tup for tup in tuples if len(tup) != k]

def main():
    n = int(input("Enter the number of tuples: "))
    tuples = []
    for _ in range(n):
        tup = tuple(input("Enter the elements of the tuple separated by space: ").split())
        tuples.append(tup)
    k = int(input("Enter the length of tuples to remove: "))
    removed_tuples = remove_tuples_of_length(tuples, k)
    print(removed_tuples)

if __name__ == "__main__":
    main()
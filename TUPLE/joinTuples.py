def join_tuples(tuples):
    result = {}
    for tup in tuples:
        if tup[0] in result:
            result[tup[0]] += tup[1:]
        else:
            result[tup[0]] = tup
    return list(result.values())

def main():
    n = int(input("Enter the number of tuples: "))
    tuples = []
    for _ in range(n):
        tup = tuple(input("Enter the elements of the tuple separated by space: ").split())
        tuples.append(tup)
    joined_tuples = join_tuples(tuples)
    print(f"The Joined Tuples: {joined_tuples}")

if __name__ == "__main__":
    main()
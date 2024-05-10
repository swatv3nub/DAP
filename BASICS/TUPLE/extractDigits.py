def extract_digits(tuples):
    return [int(item) for tup in tuples for item in tup if item.isdigit()]

def main():
    n = int(input("Enter the number of tuples: "))
    tuples = []
    for _ in range(n):
        tup = tuple(input("Enter the elements of the tuple separated by space: ").split())
        tuples.append(tup)
    digits = extract_digits(tuples)
    print(digits)

if __name__ == "__main__":
    main()
    
def evens(start, end):
    return [i for i in range(start, end + 1) if i % 2 == 0]


def main():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    result = evens(start, end)
    print("List of even numbers:", result)

if __name__ == '__main__':
    main()
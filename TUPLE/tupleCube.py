def tupleCube(numbers):
    return [(num, num ** 3) for num in numbers]

def main():
    user_input = input("Enter elements of the tuple:: ")
    numbers = list(map(int, user_input.split()))
    result = tupleCube(numbers)
    print(result)

if __name__ == "__main__":
    main()
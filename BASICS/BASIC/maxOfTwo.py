def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

def main():
    a = int(input("Enter First Number: "))
    b = int(input("Enter second number: "))
    print(f"The Maximum is {max_of_two(a, b)}")

if __name__ == "__main__":
    main()
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))


def main():
    n = int(input("Enter the value of n: "))
    result = sum_of_squares(n)
    print(f"The sum of squares of the first {n} natural numbers is: {result}")

if __name__ == '__main__':
    main()

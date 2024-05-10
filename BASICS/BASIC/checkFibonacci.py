def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def main():
    n = int(input("Enter a number: "))
    if is_fibonacci(n):
        print(n, "is a Fibonacci number")
    else:
        print(n, "is not a Fibonacci number")

if __name__ == '__main__':
    main()
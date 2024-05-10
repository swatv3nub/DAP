def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n-1]

def main():
    n = int(input("Enter a number: "))
    print(fibonacci(n))
    
if __name__ == '__main__':
    main()
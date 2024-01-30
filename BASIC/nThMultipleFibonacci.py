def fibonacci_multiple(n, multiple):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    return fib_sequence[n-1] * multiple

def main():
    n = int(input("Enter a number: "))
    multiple = int(input("Enter a multiple: "))
    print(fibonacci_multiple(n, multiple))

if __name__ == '__main__':
    main()
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    print("Prime numbers between", start, "and", end, "are:")
    print(prime_numbers)

def main():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    print_prime_numbers(start, end)

if __name__ == '__main__':
    main()

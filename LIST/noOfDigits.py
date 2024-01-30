def sum_of_digits(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += sum(int(digit) for digit in str(number))
    return total_sum

def main():
    n = int(input("Enter the number of elements in the list: "))
    numbers = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        numbers.append(element)
    result = sum_of_digits(numbers)
    print("Sum of digits of numbers:", result)

if __name__ == '__main__':
    main()

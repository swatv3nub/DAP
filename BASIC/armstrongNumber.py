def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_cubes = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_cubes == num:
        return True
    else:
        return False

def main():
    number = int(input("Enter a number: "))
    if is_armstrong_number(number):
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")

if __name__ == '__main__':
    main()
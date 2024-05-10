def cube_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum
def main():
    n = int(input("Enter the value of n: "))
    result = cube_sum(n)
    print("The cube sum of the first", n, "natural numbers is:", result)

if __name__ == '__main__':
    main()
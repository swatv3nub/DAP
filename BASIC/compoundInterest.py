def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate/100) ** time
    interest = amount - principal
    return interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (in percentage): "))
    time = float(input("Enter the time period (in years): "))
    interest = calculate_compound_interest(principal, rate, time)
    print(f"The compound interest is {interest}")
    
if __name__ == '__main__':  
    main()
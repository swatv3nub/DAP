def snkPscl(string):
    return string.title().replace("_", "")

def main():
    string = input("Enter a string: ")
    dewd = snkPscl(string)
    print(f"Pascal Form: {dewd}")

if __name__ == "__main__":
    main()
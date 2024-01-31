import re

def is_binary_string(string):
    pattern = r'^[01]+$'
    if re.match(pattern, string):
        return True
    else:
        return False

def main():
    string = input("Enter a string: ")
    if is_binary_string(string):
        print("The string is a binary string.")
    else:
        print("The string is not a binary string.")

if __name__ == "__main__":
    main()
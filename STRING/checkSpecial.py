import re

def checkSpecial(string):
    pattern = r'[^a-zA-Z0-9\s]'
    if re.search(pattern, string):
        return True
    else:
        return False

def main():
    string = input("Enter a string: ")
    if checkSpecial(string):
        print("The string contains special characters.")
    else:
        print("The string does not contain special characters.")

if __name__ == "__main__":
    main()

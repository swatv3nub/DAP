def is_symmetrical(string):
    return string == string[::-1]

def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

def main():
    input_string = input("Enter a string: ")

    if is_symmetrical(input_string):
        print("The string is symmetrical.")
    else:
        print("The string is not symmetrical.")

    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    
if __name__ == "__main__":
    main()

def is_palindrome(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    else:
        return False
def main():
    sss = input("Enter a string: ")
    if is_palindrome(sss):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
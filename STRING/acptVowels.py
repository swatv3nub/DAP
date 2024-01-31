def contains_all_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    string = string.lower()
    for i in vowels:
        if i not in string:
            return False
    return True

def main():
    input_string = input("Enter a string: ")
    if contains_all_vowels(input_string):
        print("The string contains all vowels.")
    else:
        print("The string does not contain all vowels.")

if __name__ == "__main__":
    main()

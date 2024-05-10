def replaceSubstring(string, substring, replacement):
    return string.replace(substring, replacement)

def main():
    string = input("Enter a string: ")
    substring = input("Enter a substring: ")
    replacement = input("Enter a replacement: ")
    new_string = replaceSubstring(string, substring, replacement)
    print(new_string)
    
if __name__ == "__main__":
    main()
import re

def check_url(string):
    pattern = re.compile(r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})? ') #PATTERN TAKEN FROM freeCodeCamp -_-
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False

def main():
    string = input("Enter a string: ")
    if check_url(string):
        print("The string is a URL.")
    else:
        print("The string is not a URL.")

if __name__ == "__main__":
    main()

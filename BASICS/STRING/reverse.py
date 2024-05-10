def reverse_words(string):
    words = string.split()
    rev = ' '.join(reversed(words))
    return rev

def main():
    string = input("Enter a string: ")
    print(reverse_words(string))
    
if __name__ == "__main__":
    main()

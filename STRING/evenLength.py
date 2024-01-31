def PEL(string):
    words = string.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

def main():
    string = input("Enter a string: ")
    PEL(string)

if __name__ == "__main__":
    main()

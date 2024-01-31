def split_and_join(string):
    words = string.split()
    joined_string = " -SPLIT- ".join(words)
    return joined_string

def main():
    string = input("Enter a string: ")
    joined_string = split_and_join(string)
    print(joined_string)

if __name__ == "__main__":
    main()
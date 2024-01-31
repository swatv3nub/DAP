def find_words_greater_than_length(string, k):
    words = string.split()
    result = [word for word in words if len(word) > k]
    return result

def main():
    string = input("Enter a string: ")
    k = int(input("Enter a number: "))
    result = find_words_greater_than_length(string, k)
    print(result)

if __name__ == '__main__':
    main()
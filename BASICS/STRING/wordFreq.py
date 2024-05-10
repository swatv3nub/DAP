def wordFreq(string):
    words = string.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def main():
    string = input("Enter a string: ")
    frequency = wordFreq(string)
    for word in frequency:
        print(f"{word}: {frequency[word]}")

if __name__ == "__main__":
    main()
from collections import Counter

def maxFreq(string):
    counter = Counter(string)
    max_frequent = max(counter.values())
    return [char for char, count in counter.items() if count == max_frequent]

def main():
    string = input("Enter a string: ")
    max_frequent = maxFreq(string)
    print(f"The max frequent character in '{string}' is '{max_frequent}'")

if __name__ == "__main__":
    main()
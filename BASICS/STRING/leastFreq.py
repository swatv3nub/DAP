from collections import Counter

# def leastFreq(string):
#     counter = Counter(string)
#     least_frequent = min(counter, key=counter.get)
#     return least_frequent

def leastFreq(string):
    counter = Counter(string)
    least_frequent = min(counter.values())
    return [char for char, count in counter.items() if count == least_frequent]

def main():
    string = input("Enter a string: ")
    least_frequent = leastFreq(string)
    print(f"The least frequent character in '{string}' is '{least_frequent}'")

if __name__ == "__main__":
    main()
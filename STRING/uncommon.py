def find_uncommon_words(str1, str2):
    # Split the strings into words
    words1 = str1.split()
    words2 = str2.split()
    set1 = set(words1)
    set2 = set(words2)
    uncommon_words = set1.symmetric_difference(set2)

    return uncommon_words

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    uncommon_words = find_uncommon_words(str1, str2)
    print("Uncommon words:", uncommon_words)

if __name__ == "__main__":
    main()

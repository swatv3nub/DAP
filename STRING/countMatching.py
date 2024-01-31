def CMC(string1, string2):
    count = 0
    for char1 in string1:
        if char1 in string2:
            count += 1
            string2 = string2.replace(char1, '', 1)
    return count

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    print(f"{CMC(string1, string2)} characters are matching.")

if __name__ == "__main__":
    main()
def check_substring(str, ss):
    if ss in str:
        return True
    else:
        return False

def main():
    s = input("Enter a string: ")
    ss = input("Enter a substring: ")
    if check_substring(s, ss):
        print(f"The substring '{ss}' is in the string '{s}'.")
    else:
        print(f"The substring '{ss}' is not in the string '{s}'.")

if __name__ == "__main__":
    main()

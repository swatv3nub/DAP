def is_empty_string(string):
    if len(string) == 0:
        return True
    else:
        return is_empty_string(string[1:])

def main():
    string = input("Enter a string: ")
    if is_empty_string(string):
        print("The string can become empty by recursive deletion")
    else:
        print("The string cannot become empty by recursive deletion")

if __name__ == '__main__':                                                                       
    main()
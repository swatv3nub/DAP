def remove_nth_character(string, n):
    return string[:n] + string[n+1:]

def main():
    string = input("Enter a string: ")
    n = int(input("Enter the index of the character to remove: "))
    print(remove_nth_character(string, n))
    
if __name__ == '__main__':
    main()

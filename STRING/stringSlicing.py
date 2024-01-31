def rotate_string(s, k):
    n = len(s)
    k = k % n
    rotated = s[k:] + s[:k]
    return rotated

def main():
    string = input("Enter a string: ")
    k = int(input("Enter a number: "))
    rotated = rotate_string(string, k)
    print(rotated)
    
if __name__ == '__main__':
    main()

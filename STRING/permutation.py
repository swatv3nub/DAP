import itertools

def generate_permutations(string):
    chars = list(string)
    permutations = itertools.permutations(chars)
    result = [''.join(perm) for perm in permutations]
    return result

def main():
    string = input("Enter a string: ")
    permutations = generate_permutations(string)
    print(permutations)
    
if __name__ == "__main__":
    main()

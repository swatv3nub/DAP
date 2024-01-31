import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_until_match(target_string):
    generated_string = ""
    while generated_string != target_string:
        generated_string = generate_random_string(len(target_string))
        print(generated_string)

def main():
    target_string = input("Enter the target string: ")
    generate_until_match(target_string)
    
if __name__ == "__main__":
    main()

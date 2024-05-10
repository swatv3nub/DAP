

# def remDupes(string):
#     unique_chars = set(string)
#     return ''.join(unique_chars)

"""REMOVED THE ABOVE CODE AND REPLACED IT WITH THE BELOW CODE, AS THE ABOVE CODE DOES NOT PRESERVE THE ORDER OF THE CHARACTERS IN THE STRING"""

import re
def remDupes(string):
    pattern = r'(\b\w+\b)(?=.*\b\1\b)' #PATTERN TAKEN FROM REGEX101 -_-
    replaced_string = re.sub(pattern, '', string)
    return replaced_string


def main():
    string = input("Enter a string: ")
    print(remDupes(string))
    
if __name__ == "__main__":
    main()
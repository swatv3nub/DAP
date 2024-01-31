def replace_words_with_K(text, words):
    for i in words:
        text = text.replace(i, "K")
    return text

def main():
    text = input("Enter a string: ")
    text = text.lower()
    words = input("Enter words to replace separated by spaces: ").split()
    for i in words:
        i = i.lower()
    text = replace_words_with_K(text, i)
    print(text)
    
if __name__ == '__main__':
    main()

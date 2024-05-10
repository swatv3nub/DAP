def size(t):
    return len(t)

def main():
    user_input = input("Enter elements of the tuple: ")
    elements = user_input.split(" ")
    my_tuple = tuple(elements)
    size = size(my_tuple)
    print("Size of the tuple is:", size)

if __name__ == "__main__":
    main()

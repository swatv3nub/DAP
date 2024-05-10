def sort_by_second(L):
    return sorted(L, key=lambda x: x[1])

def main():
    user_input = input("Enter elements of the tuple: ")
    elements = user_input.split(" ")
    my_tuple = tuple(elements)
    size = size(my_tuple)
    print("Size of the tuple is:", size)
    print("Elements in ascending order are:")
    print(sort_by_second(my_tuple))

if __name__ == "__main__":
    main()
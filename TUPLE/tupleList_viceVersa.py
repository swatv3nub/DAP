def add_tuple_to_list(new_tuple, new_list):
    new_list.append(new_tuple)
    return new_list

def add_list_to_tuple(new_list, new_tuple):
    new_tuple += tuple(new_list)
    return new_tuple

def main():
    tuple_elements = input("Enter tuple elements: ").split(" ")
    new_tuple = tuple(tuple_elements)
    list_elements = input("Enter list elements: ").split(" ")
    new_list = list(list_elements)
    switch = {
        '1': add_tuple_to_list,
        '2': add_list_to_tuple
    }

    choice = input("Enter 1 to add tuple to list, 2 to add list to tuple: ")

    func = switch.get(choice, lambda: "Invalid choice")
    print(func(new_tuple, new_list))

if __name__ == "__main__":
    main()
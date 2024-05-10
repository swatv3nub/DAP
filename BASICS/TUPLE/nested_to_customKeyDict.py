def nested_tuple_to_dict(tuples, keys):
    return {key: value for key, value in zip(keys, tuples)}

def main():
    tuples = eval(input("Enter a nested tuple: "))
    keys = input("Enter the keys separated by space: ").split()
    custom_dict = nested_tuple_to_dict(tuples, keys)
    print(custom_dict)

if __name__ == "__main__":
    main()
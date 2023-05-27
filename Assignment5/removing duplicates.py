def remove_duplicates(input_list):
    unique_list = sorted(list(set(input_list)))
    return unique_list

def main():
    input_list = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    unique_list = remove_duplicates(input_list)
    print("Unique sorted list:", unique_list)

if __name__ == "__main__":
    main()

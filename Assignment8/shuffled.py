import random

def shuffle_list(lst):
    new_lst = lst.copy()
    for i in range(len(new_lst) - 1, 0, -1):
        j = random.randint(0, i)
        new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
    return new_lst

def main():
    original_list = [1, 2, 3, 4, 5]
    shuffled_list = shuffle_list(original_list)
    print(shuffled_list[-1])


if __name__ == '__main__':
    main()

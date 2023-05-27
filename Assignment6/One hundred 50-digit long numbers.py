if __name__=="__main__":
    with open('input.txt', 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    sum_numbers = sum(numbers)
    first_ten_digits = str(sum_numbers)[:10]

    print(first_ten_digits)

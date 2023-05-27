def main():
    num = 2 ** 1000
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)

    print(digit_sum)


if __name__ == '__main__':
    main()

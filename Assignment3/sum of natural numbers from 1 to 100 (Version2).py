def main():
    total = 0
    for num in range(1, 101):
        digits = list(str(num))
        for digit in digits:
            total += int(digit)
    print(total)


if __name__ == "__main__":
    main()
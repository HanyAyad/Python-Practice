

def main():
    while True:
        try:
            number1 = float(input("First Number: "))
            number2 = float(input("Second Number: "))
            res = number1 / number2
            print('Division result: {0:.2f}'.format(res))
            print('-' * 10)
        except ZeroDivisionError:
            print("Divisor can't be Zero")
        else:
            print("Everything works fine")

#####

if __name__ == "__main__":
    main()
def sum_of_digits(exponent):
    """
    This program calculates the sum of the digits of the number 2^exponent.
    """
    number = pow(2, exponent)
    number_sum = 0
    for digit in str(number):
        number_sum += int(digit)
    return number_sum

if __name__ == '__main__':
    print(sum_of_digits(1000))

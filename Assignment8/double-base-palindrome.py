def check_palindrome(n):
    return str(n) == str(n)[::-1]

def check_binary_palindrome(n):
    binary_str = bin(n)[2:]
    return binary_str == binary_str[::-1]

def main():
    double_base_palindromes = []
    for i in range(1, 1000000):
        if check_palindrome(i) and check_binary_palindrome(i):
            double_base_palindromes.append(i)

    print(sum(double_base_palindromes))


if __name__ == '__main__':
    main()

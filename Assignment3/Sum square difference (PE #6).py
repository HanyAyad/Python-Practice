def sum_square_difference(n):
    sum_of_squares = n*(n+1)*(2*n+1)//6
    square_of_sum = (n*(n+1)//2)**2
    difference = square_of_sum - sum_of_squares
    return difference

def main():
    n = 100
    difference = sum_square_difference(n)
    print("The difference between the sum of the squares of the first", n, "natural numbers and the square of the sum is:", difference)

if __name__ == '__main__':
    main()

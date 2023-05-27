def is_munchausen(num):
    digits = [int(d) for d in str(num)]
    sum = 0
    for d in digits:
        sum += d ** d
    return sum == num
def get_all_munchausen():
    print('0 is munchausen')
    for i in range(1,440 * (10**6)):
        if is_munchausen(i):
            print(f'{i} is munchausen')
def main():
   print(get_all_munchausen())

if __name__ == '__main__':
    main()
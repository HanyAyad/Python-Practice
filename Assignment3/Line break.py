import sys
import random as r

def main():
    maxDigits = 100
    maxLength = 10
    lineLength = 0
    for i in range(maxDigits):
        print(r.randint(0, 9), end="")
        lineLength += 1
        if lineLength == maxLength:
            print()
            lineLength = 0
    if lineLength > 0:
        print()

if __name__ == '__main__':
    main()

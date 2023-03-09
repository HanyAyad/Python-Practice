
def reverse(s):
    string=f"{s}"
    res=s[::-1]
    return int(res)


def main():
    s= input("Enter your number: ").strip() 
    print(reverse(s))

if __name__ == "__main__":
    main()
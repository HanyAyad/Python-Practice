def numerdigit(s):
    string=f"{s}"
    return len(string)

def main():
    s=2**256
    print(numerdigit(s))

if __name__ == "__main__":
    main()
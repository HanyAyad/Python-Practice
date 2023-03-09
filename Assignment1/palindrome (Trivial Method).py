
def is_palindrome(s):
    return s == s[::-1]

def main():
    word = input("Enter A word: ").strip() 
    check=is_palindrome(word.lower())
    if check==True:
        res="palindrome"
    else : 
        res="not palindrome"
    print(f"The word {word} is {res}!")

if __name__ == "__main__":
    main()
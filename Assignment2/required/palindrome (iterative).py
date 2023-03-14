def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

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
def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    '''This program contains a function 'valid' that takes two arguments: 'text' and 'chars'.
        The 'valid' function returns a string that contains only the characters from the 'text' argument that are present in the 'chars' argument.'''
    return ''.join(filter(lambda x: x in chars, text))

def main():
    text = "Barking!"
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    print(valid(text, chars))  # "B"

    text = "KL754"
    chars = "0123456789"
    print(valid(text, chars))  # "754"

    text = "BEAN"
    chars = "abcdefghijklmnopqrstuvwxyz"
    print(valid(text, chars))  # ""

if __name__ == '__main__':
    main()

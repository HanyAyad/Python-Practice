def decode_message(message):

    letters = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = ''

    for c in message:
        if c.isalpha() and c.islower():
            index = (letters.index(c) + 2) % 26
            plaintext += letters[index]
        elif c.isalpha() and c.isupper():
            index = (letters.index(c.lower()) + 2) % 26
            plaintext += letters[index].upper()
        else:
            plaintext += c
    return plaintext

           
def main():
    message='''Bcyp Qml,

G fytc y dyrfcpjw ybtgac dmp wms:
jcypl rfc Nwrfml npmepykkgle jylesyec!

Jmtc,

Byb'''
    print(decode_message(message))

if __name__ == "__main__":
    main()
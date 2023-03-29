def xor_operation(var1, var2):
    if bool(var1) != bool(var2):
        print("Yes, One variable is True and the other is False")
    else:
        print("Both variables are either True or False")

def main():
    # Given variables
    str1 = "python"
    str2 = None

    # Call the XOR function
    xor_operation(str1, str2)

if __name__ == '__main__':
    main()

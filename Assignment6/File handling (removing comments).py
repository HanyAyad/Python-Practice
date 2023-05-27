if __name__=="__main__":
    with open('string1.py', 'r') as INPUT, open('string1_clean.py', 'w') as OUTPUT:
        for lines in INPUT:
            line = lines.strip()
            if not line.startswith('#'):
                OUTPUT.write(line+"\n")

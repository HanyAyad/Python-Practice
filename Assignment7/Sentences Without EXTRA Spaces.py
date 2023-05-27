def remove_extra_spaces(sentence):
    return " ".join(sentence.split())
def main():
    print(remove_extra_spaces('I  like   python'))
    
if __name__=="__main__":
    main()
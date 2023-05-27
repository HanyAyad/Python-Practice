def normalize(string):
    return "".join(char.lower() for char in string if char.isalpha())


def is_anagram(str1, str2):
    str1 = normalize(str1)
    str2 = normalize(str2)

    if len(str1) != len(str2):
        return False

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    return sorted_str1 == sorted_str2

def main():
    print(is_anagram("listen","Silent"))
    print(is_anagram("A gentleman","Elegant Man"))
    print(is_anagram("Clint Eastwood","Old West Action"))
    print(is_anagram("Dog","Fog"))
    
if __name__=="__main__":
    main()
    
if __name__ == "__main__":
    
    """Ex1: Convert vehicle names to uppercase and append an exclamation mark"""
    vehicle=['car', 'tram', 'metro']
    capVehicle=[s.upper()+'!' for s in vehicle]
    print(capVehicle)

    """Ex2: Capitalize the first letter of each name"""
    names=['mario', 'luigi', 'peach']
    capNames=[s.capitalize() for s in names]
    print(capNames)

    """Ex3: Create a list of 10 zeros using two different methods"""
    zeros=[0 for n in range(10)]
    zeros2=[0]*10
    print(zeros)
    print(zeros2)

    """Ex4: Create two lists, one with the numbers 1 to 10 and another with their respective multiples of 2"""
    numbers= [n for n in range(1,11)]
    numbers2= [n*2 for n in range(1,11)]

    print(numbers)
    print(numbers2)

    """Ex5: Convert a list of strings to a list of integers"""
    charList= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    intList=[int(n) for n in charList]
    print(charList)
    print(intList)

    """Ex6: Convert a string of digits to a list of integers"""
    str1="1234567"
    num1=[int(n) for n in str1]
    print(num1)
    
    """Ex7: Create a list of word lengths from a sentence"""
    sentence = 'The quick brown fox jumps over the lazy dog'
    word_lengths = [len(word) for word in sentence.split()]
    print(word_lengths)
    
    """Ex8: Create a list of first characters of each word in a sentence"""
    sentence = "python is an awesome language"
    first_chars = [word[0] for word in sentence.split()]
    print(first_chars)
    
    """Ex9: Create a list of word and length tuples from a sentence"""
    sentence = 'The quick brown fox jumps over the lazy dog'
    word_tuples = [(word, len(word)) for word in sentence.split()]
    print(word_tuples)

    """Ex10: Create a list of even numbers from 0 to 10"""
    list1=[n for n in range(10) if n%2==0]
    print(list1)

    """Ex11: Create a list of even squares from 0 to 19"""
    even_squares = [num**2 for num in range(20) if (num**2)%2 == 0]
    print(even_squares)
    
    """Ex12: Create a list of squares ending with 4 from 0 to 19"""
    squares_ending_with_4 = [num**2 for num in range(20) if str(num**2)[-1] == '4']
    print(squares_ending_with_4)
    
    """Ex13: Create a string containing uppercase letters from A to Z"""
    uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    uppercase_string = ''.join(uppercase_letters)
    print(uppercase_string)
    
    """Ex14: Remove leading and trailing spaces from each element in a list of strings"""
    words_with_spaces = [' apple ', ' banana ', ' kiwi']
    no_spaces = [word.strip() for word in words_with_spaces]
    print(no_spaces)

    
    """Ex15 Convert the following list of binary digits into a string of characters:"""
    lst = [1, 0, 1, 1, 0, 1, 0, 0]
    result = ''.join(str(i) for i in lst)
    print(result)









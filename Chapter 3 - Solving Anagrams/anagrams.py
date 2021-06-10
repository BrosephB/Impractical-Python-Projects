from load_dictionary import load 

# load the dictionary file as a list of words
dictList = load('./dictionary.txt')

def findAnagrams(word,dictList):
    """
    Takes a word and a list of words as input and returns a list of anagrams 
    found in the dictionary list of words dictList
    """
    anagrams = []
    userList = list(word)
    for dictWord in dictList:
        charList = list(dictWord)
        
        # if the sorted lists are equal but the words aren't the same
        if userList != charList and sorted(userList) == sorted(charList):
            anagrams.append(dictWord)
    
    return anagrams

flag = True 
while flag:
    userWord = input("\nPlease enter a word for which you'd like to find anagrams for: ")
    anagrams = findAnagrams(userWord,dictList)    
    if len(anagrams) >= 1:
        print("We found the following anagrams: ")
        for anagram in anagrams:
            print(anagram)
    else:
        print("Sorry I found no anagrams for that word")
        
    try_again = input("Press enter to try again, or enter 'q' to quit the program \n")
    if (try_again.lower()).strip() == 'q':
        flag = False


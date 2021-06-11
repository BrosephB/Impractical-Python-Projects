"""
phraseAnagrams.py - User can interactively find anagram phrases to their name
Input required: user name input, dictionary file
Output expected: a phrase that is an anagram of the input
"""
import sys
from collections import Counter
from load_dictionary import load 

dictList = load("./dictionary.txt")

# ensure that the dictionary contains lowercase 'a' and 'I'
dictList.append('a')
dictList.append('i')
dictList = sorted(dictList)

userName = input("Please enter the name for which you'd like to find an anagram phrase: ")

def findAnagrams(name,wordList):
    """Read name and dictionary file to display all anagrams which are a subset of the name"""
    nameLetterMap = Counter(name)
    anagramPhrase = [] 
    for word in wordList:
        test = ''
        wordLetterMap = Counter(word.lower())
        for letter in word:
            if wordLetterMap[letter] == nameLetterMap[letter]:
                test += letter 
        if Counter(test) == wordLetterMap:
            anagramPhrase.append(word)
    print(*anagramPhrase,sep='\n')
    print()
    print("Remaining letters = {}".format(name))
    print("Number of remaining letters = {}".format(len(name)))
    print("Number of remaining (real word) anagrams = {}".format(len(anagramPhrase)))

def processChoice(name):
    """Check choice for validity. Returns choice + remaining letters"""
    flag = True
    while flag:
        choice = input('\nPlease make a choice, press Enter to start over, or q to quit program:')
        if choice =="":
            main()
        elif choice == "q":
            sys.exit(0)
        else:
            candidate = ''.join(choice.lower().split())
            leftOverList = list(name)
            for letter in candidate:
                if letter in leftOverList:
                    leftOverList.remove(letter)
            if len(name) - len(leftOverList) == len(candidate):
                flag == False
                break
            else:
                print("Won't work! Please make another choice")
    name = ''.join(leftOverList)
    return choice, name

def main():
    """Help user build anagram phrase from their name"""
    name = ''.join(userName.lower().split())
    name = name.replace('-','')
    limit = len(name)
    phrase = ''
    running = True
    
    while running:
        tempPhrase = phrase.replace(' ', '')
        if len(tempPhrase) < limit:
            print("Length of anagram phrase = {}".format(len(tempPhrase)))
            
            findAnagrams(name,dictList)
            print("Current anagram phrase =", end=" ")
            print(phrase)
            choice, name = processChoice(name)
            phrase += choice + ' '
        elif len(tempPhrase) == limit:
            print("\n*****Job Complete!!!*****\n")
            print("Anagram of name =", end=" ")
            print(phrase)
            print()
            tryAgain = input('\n\nTry again? (Press Enter to try again or "q" to quit)\n ')
            if tryAgain.lower() == 'q':
                running = False
                sys.exit()
            else:
                main()

if __name__ == '__main__':
    main()
            
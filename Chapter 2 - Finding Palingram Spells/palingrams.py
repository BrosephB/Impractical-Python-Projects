"""
Palingrams.py - Finds all word-pair palingrams in a dictionary file
"""
import load_dictionary as ld
import sys 

wordList = ld.load('./dictionary.txt')

# find word-pair palingrams

def findPalingrams():
    """
    Find dictionary palingrams
    """
    paliList = []
    words = set(wordList) # converting this list into a set will speed up runtime significantly
    for word in words:
        end = len(word)
        revWord = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == revWord[:end-i] and revWord[end-i:] in words:
                    paliList.append((word,revWord[end-i:]))
                if word[:i] == revWord[end-i:] and revWord[:end-i] in words:
                    paliList.append((revWord[:end-i],word))
    return paliList 

palingrams = findPalingrams()

# sort the palingrams alphabetically

palingrams = sorted(palingrams)
print("We have found {} Palingrams\n".format(len(palingrams)))
for first, second in palingrams:
    print(first,second)
input("\nPress enter to exit the program \n")
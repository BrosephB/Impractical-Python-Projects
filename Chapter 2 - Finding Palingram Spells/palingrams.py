"""
based on a dictionary list of words, this program will find palindromes
"""
import sys
from load_dictionary import load 

wordList = load('./dictionary.txt')
paliList = []
# finding out if a word in the list is a palindrome
for word in wordList:
    word = word.strip()
    wordLen = len(word)
    if len(word) > 1 and word == word[::-1]:  # same forwards as it is backwards
        paliList += word
        print("Palindrome found: {}".format(word))
print("Number of Palindromes found: {}".format(len(paliList)))
        
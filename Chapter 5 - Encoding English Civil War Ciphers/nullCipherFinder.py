import string 
import sys

def loadTextFile(file):
    """load a text file as a string"""
    
    with open(file) as f:
        return f.read().strip()

def verifyExit(inputString):
    if inputString.lower().strip() == 'q':
        sys.exit(0)

def findMessage(text,numLetters):
    """using the number of letters after the punctuation mark to examine (provided by user)
    find the message and return a list of the deciphered words"""
    text = ''.join(text.split())
    # loop through the letters by the amount specified
    for i in range(1,numLetters+1):
        translation = ""
        count = 0
        foundPunc = False   # found punctuation mark?
        for character in text:
            if character in string.punctuation:
                count = 0
                foundPunc = True
            elif foundPunc:
                count += 1
            if count == i:
                translation += character 
    return translation

def display(fullMessageList):
    message = ' '.join(fullMessageList)
    assert message != ""
    print(message)

def main():
    """Program's main function"""
    
    # show user the ciphertext and ask how many letters after the punctuation to search for
    CIPHER_TEXT_ADDRESS = "./ciphertext.txt"
    cipherText = loadTextFile(CIPHER_TEXT_ADDRESS)
    print("The ciphertext is:\n\n")
    print(cipherText)
    print()
    
    # while loop is broken when q is entered
    while True:
        print("Enter 'q' into the program if you wish to exit")
        numLetters = input("How many letters after the punctuation mark would you like to examine? ")
        
        # check and verify input
        verifyExit(numLetters)
        if numLetters.isdigit():
            numLetters = int(numLetters)
        else:
            print("\nPlease Try again and Input a Whole Number")
            continue
        
        messageList = findMessage(cipherText,numLetters)
        
        # display final decoded message
        print("The message from this is:\n\n")
        display(messageList)
        print()

main()
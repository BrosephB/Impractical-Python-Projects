"""
railFenceCypherEncrypt.py

this is for a two-rail fence cipher for short messages
Example text to encrypt: 'Buy more Maine potatoes'
Rail fence style: B Y O E A N P T T E
U M R M I E O A O S
Read zigzag: \/\/\/\/\/\/\/\/\/\/
Encrypted: BYOEA NPTTE UMRMI EOAOS

Input: requires a string to encode
Output: gives a string that is a cipher of the original input
"""

def prepMessage(message):
    """ Message will be stripped of all whitespace and capitalized"""
    message = ''.join(message.split())
    message = message.strip()
    message = message.upper()
    return message 

def buildRails(message):
    """Message will be divided via the 2 rail method"""
    topList = message[::2]
    bottomList = message[1::2]
    rails = topList + bottomList 
    return rails

def encyrpt(rails):
    """takes in rails as input and outputs the ciphertext divided into groups of five"""
    cipherText = ' '.join([rails[i:i+5] for i in range(0,len(rails),5)])
    return cipherText

def main():
    """run the main program"""
    
    # obtain user input and format the input to be encrypted
    message = input("Please enter your message to be encoded with the rail fence cipher: ")
    plainText = prepMessage(message)
    print("Plaintext: {} ".format(plainText))
    
    # take this new formatted input and encrypt, then show the result
    rails = buildRails(plainText)
    print("\n\n***Please wait while we encrypt***\n\n")
    cipherText = encyrpt(rails)
    print("Ciphertext: {} ".format(cipherText))

if __name__ == "__main__":
    main()
    input()
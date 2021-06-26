
# Impractical Python Projects
As a part of learning python, It's important to make lots of projects no matter how small or seemingly impractical. This repository contains all the project work I have done when working through the book *Impractical Python* by Lee Vaughan. I never intended on finishing the book, so I have just done enough projects to gain more experience with mini projects and I can move on to further learning and projects outside of this book.

![Impractical Python Projects Book by Lee Vaughan](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/IPJ.jpg?raw=true)

### Chapter 1 - Silly Name Generator

the program begins by generating a silly nickname for you.
If you don't like the first nickname, simply press enter to generate a new one!

![End of Silly Name Generator Program](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterOne_2.png?raw=true)

It's just as easy as the press of a button to generate a nickname or quit the program

### Chapter 2- Finding Palingram spells
There were a lot of little projects involved in this chapter 

Palindromes.py required a custom module called load_dictionary.py and a text file full of words in the English language called dictionary.txt. Palindromes.py used these files to find and display palindromes in the English language. Palindromes are words that spell the same word forwards and backwards, such as "Dad" or "reviver"

![Screenshot of Palindromes.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterTwo_1.png?raw=true)

Palingrams.py also used the same dictionary files, but now the program found word pairs of palindromes, called palingrams. Examples include "race car" and "nurses run" because the phrases spell the same way forwards and backwards.

![Screenshot of Palingrams.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterTwo_2.png?raw=true)

The solution for this code initially had a runtime of about 3 minutes. This issue was solved easily by using sets as opposed to lists to check whether a certain word existed in the dictionary or not and now the runtime is under a second. Optimizing code like this to improve runtime is part of the iterative coding process. 

### Chapter 3 - Solving Anagrams

First, this chapter gave the task of creating a program that loads the same dictionary file as the last chapter. My version of the program takes a word as user input, and displays all anagrams found in the dictionary. I also refactored the code into a function so that the function can easily be called over and over again, so the user can continue to use the program until they choose to quit.

![Screenshot of anagrams.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterThree_1.png?raw=true)

Next, this chapter gave the task of creating a program that, instead of finding anagrams that are single words, you can input you name, and interactively create a phrase which is an anagram of your name. I entered the name "Sir Arthur Conan Doyle", the author of the _Sherlock Holmes_ series. With more tries and more time, I could probably come up with something more sensible, but as you can see, I've found the anagram "actual horror side" from "Sir Arthur Conan Doyle". This was fun to play around with

![first Screenshot of anagramPhrases.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterThree_2.png?raw=true)

![Second Screenshot of anagramPhrases.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterThree_3.png?raw=true)

![Third Screenshot of anagramPhrases.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterThree_4.png?raw=true)

![Fourth Screenshot of anagramPhrases.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterThree_5.png?raw=true)

### Chapter 4 - Decoding American Civil War Ciphers

In this chapter there is routeCipherDecrypt.py which works on the idea of route transposition ciphers such as those used during the American civil war. Transposition ciphers involve taking a plaintext (our "real" message) then putting the words in that plaintext into a matrix, and by essentially "transposing" the way we read the words in the matrix, we get a reconstruction of our original message (a cipher text). To show this transposition in python, we start with a certain cipher text that has no meaning and you can see that the resulting plain text is in a different arrangement. The arrangement can be changed simply by changing the numbers of the rows and columns of the matrix we will use, and even a key to indicate in what order we will read along the matrix. 

![Screenshot of routeCipherDecrypt.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterFour_1.png?raw=true)

![Screenshot of routeCipherDecrypt.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterFour_2.png?raw=true)

There is also railFenceCipherEncrypt.py which uses letter transposition ciphering instead of word transposition ciphering. The program takes user input for any message that they would like encrypted. This rail fence cipher is a 2 rail fence cipher. The cipher at the end will be five seemingly random letters grouped together.

![Screenshot of railFenceCipherEncrypt.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterFour_3.png?raw=true)

### Chapter 5 - Encoding English Civil War Ciphers

The Trevanion Cipher is a type of null cipher, which is not really much of a cipher at all, according to the author. Essentially, there is a hidden message in this seemingly innocent message at the start. To crack the code, one must examine each letter 3 characters (not including spaces) after a punctuation mark. In nullCipherFinder.py, you can experiment with a different number of character offset to examine. However, you'll likely find that 3 is the only one that can give a coherent message that says "panel at the chapel slides"

![Screenshot of nullCipherFinder.py](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterFive_1.png?raw=true)


### Chapter 6 - Writing in Invisible Ink

This is a very interesting chapter. Now instead of dealing with plain text files, we use the powers of rich text in Microsoft Word to hide a real important message inside of a document with a seemingly innocent fake message. The program uses the python-docx module and is inspired by the vignere cipher found in an episode of _Elementary_. The strategy is that in between the paragraphs of the fake message, there is a real hidden message that has the same colour as the document background and to the naked eye, it simply looks like whitespace and paragraph line breaks. The program elementary_ink.py produces the word document ciphertext_message_letterhead.docx. 

Message shown to the naked eye
![Screenshot of ciphertext_message_letterhead.docx](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterSix_1.png?raw=true)

Fake Message revealed 
![Screenshot of ciphertext_message_letterhead.docx](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterSix_2.png?raw=true)

### Chapter 7 - Breeding Giant Rats with Genetic Algorithms

This chapter used the concept of genetic algorithms to breed rats that would achieve a certain weight goal. Essentially, the program simulates generations of rats breeding, wherein we have an initial population, and this population breeds. As the population breeds, the lesser fit (lower weight) rats would die off. Depending on the weight goal set at the very beginning by the programmer, it could take many generations for the rats to achieve the weight goal. To spice things up a bit, there are skewing of statistics to make it more likely for new rats to be lighter rather than heavier, and a very small percentage of the population experiences mutations, and an even smaller percentage of that population experiences beneficial mutations (getting heavier)

![Screenshot of superRats.docx](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterSeven_1.png?raw=true)

![Screenshot of superRats.docx](https://github.com/BrosephB/Impractical-Python-Projects/blob/main/Readme/ChapterSeven_2.png?raw=true)








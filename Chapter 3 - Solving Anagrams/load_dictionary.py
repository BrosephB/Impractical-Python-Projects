"""
Load_Dictionary.py
Loads a text file as a list

input: text file name and optionally the path
Exception will raise if file can't load
Output: Returns a list of all the text in lower case
"""

import sys

def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt 
    except IOError as e:
        print("{}\nError opening {}, Terminating Program...".format(e,file))
        sys.exit(1)
        
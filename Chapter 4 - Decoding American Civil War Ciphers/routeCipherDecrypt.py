"""Decrypt a path through a Union Route Cipher
    
    Designed for wholeword
transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top & read down.
Example below is for 4x4 matrix with key 1
2 3
4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.
1 2 3 4
___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START END
Required inputs a
text message, # of columns, # of rows, key string
Prints translated plaintext
"""
import sys


ciphertext = "My Sepehr code in and name Python I is"

# split elements into words, not letters
cipherList = list(ciphertext.split())

# initializing variables
COLS = 3
ROWS = 3
key = '1 -2 -3'       # negative means read up or backwards on the row/column

def main():
    """Run main program and print decrypted plaintext."""
    
    print("\nCiphertext = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))
    print("Trying key = {}".format(key))
    
    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)
    print("Plaintext = {}".format(plaintext))

def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher): # range excludes 1 column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print("\nLength of cipher = {}".format(len_cipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    
    if ROWS * COLS != len_cipher:
        print("\nError Input columns & rows not factors of length of cipher. Terminating program.")
        sys.exit(1)

def key_to_int(key):
    """Turn key into list of integers & check validity."""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS or 0 in key_int:
        print("\nError Problem with key. Terminating.")
        sys.exit(1)
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists."""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0: # read bottom to top of column
            col_items = cipherlist[start:stop]
        elif k > 0: # read top to bottom of columnn
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k)-1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext

if __name__ == "__main__":
    main()
    input()
from includes import *

def translate(plaintext: str) -> str:
    """
    Description
    ------------
    Translates a string from plaintext to morse code
    
    Parameters
    ------------
    plaintext : str
        The original text to be translated
        
    Returns
    ------------
    morse : str
        The morse code translation of the plaintext
        
    Raises
    ------------
    Invalid character
        If a given plaintext character cannot be found 
        in the morse code lookup table
    """

    # force lowercase plaintext
    plaintext = plaintext.lower()

    # set up list for morse output
    morse = []

    # iterate through plaintext characters, adding spaces
    try:
        for char in plaintext:
            if char == ' ':
                morse.append('    ')
            else:
                morse.append(morsetable[char])
            morse.append('   ')
    except KeyError:
        print(f"Invalid character {char}. Blendermorse currently supports numbers and English letters.")

    # combine into one string and return
    return ''.join(morse)

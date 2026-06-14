# Main backend functions for morse
# translation and keyframe insertion

# Imports
from includes import *

# Constants
DIT = 1
DAH = 3
LETTERSPACE = 1
WORDSPACE = 5


def insert_keys(): #TODO: figure out how to get params from menus

    # set up inputs???
    
    # get active object
    object = bpy.context.active_object

    # insert keys
    current_frame = start_point

    for char in morse:
        match char:
            case '.':
                object.chosen_property = high
                object.keyframe_insert(data_path = chosen_property, frame = current_frame)
                current_frame = current_frame + time_unit * DIT + smoothing

            case '-':
                object.chosen_property = high
                object.keyframe_insert(data_path = chosen_property, frame = current_frame)
                current_frame = current_frame + time_unit * DAH + smoothing

            case ' ':
                object.chosen_property = low
                object.keyframe_insert(data_path = chosen_property, frame = current_frame)
                current_frame = current_frame + time_unit * LETTERSPACE + smoothing

            case '/':
                object.chosen_property = low
                object.keyframe_insert(data_path = chosen_property, frame = current_frame)
                current_frame = current_frame + time_unit * WORDSPACE + smoothing
            
            case _:
                print(f"Invalid character in morse string {char}") #TODO: output to blender GUI


        # add space
        object.chosen_property = low
        object.keyframe_insert(data_path = chosen_property, frame = current_frame)
        current_frame = current_frame + time_unit * DIT + smoothing


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
                morse.append('/')
            else:
                morse.append(morsetable[char])
            morse.append(' ')

    except KeyError:
        print(f"Invalid character {char}. Blendermorse currently supports numbers and English letters.")

    # combine into one string and return
    return ''.join(morse)


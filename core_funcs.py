# Main backend functions for morse
# translation and keyframe insertion

# Imports
from includes import *

# Constants
DIT = 1
DAH = 3
LETTERSPACE = 1
WORDSPACE = 5


def insert_keys(obj, morse: str, start_point: int, high: float, low: float, chosen_property: str, time_unit: int, smoothing: int):
    """
    Description
    ------------
    Inserts keyframes for morse code
    
    Parameters
    ------------
    obj
        The active object to be keyframed
    
    morse : str
        The morse code string to be implemented

    start_point : str
        The frame to begin inserting keyframes at

    high_val : float
        The high or "on" value to set keyframes to

    low_val : float
        The low or "off" value to set keyframes to

    chosen_property : str
        The property to animate, default is emission strength

    time_unit : int
        The base time unit in frames, equivalent to one dit

    smoothing : int
        The number of frames between high and low points
        Cannot be greater than time_unit
    """
    
    # set up inputs???

    # insert keys
    current_frame = start_point

    for char in morse:
        match char:
            case '.':
                obj.chosen_property = high
                obj.keyframe_insert(data_path = chosen_property, frame = current_frame)
                current_frame = current_frame + time_unit * DIT + smoothing

            case '-':
                obj.chosen_property = high
                obj.keyframe_insert(data_path = chosen_property, frame = current_frame)
                current_frame = current_frame + time_unit * DAH + smoothing

            case ' ':
                obj.chosen_property = low
                obj.keyframe_insert(data_path = chosen_property, frame = current_frame)
                current_frame = current_frame + time_unit * LETTERSPACE + smoothing

            case '/':
                obj.chosen_property = low
                obj.keyframe_insert(data_path = chosen_property, frame = current_frame)
                current_frame = current_frame + time_unit * WORDSPACE + smoothing
            
            case _:
                print(f"Invalid character in morse string {char}") #TODO: output to blender GUI


        # add space
        obj.chosen_property = low
        obj.keyframe_insert(data_path = chosen_property, frame = current_frame)
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

def button_run(plaintext: str, start_point: int, high_val: float, low_val: float, chosen_property: str, time_unit: int, smoothing: int):
    """
    Description
    ------------
    Wrapper function that runs internal scripts for
    translation/keyframing when UI button is pressed

    Parameters
    ------------
    plaintext : str
        The original text to be translated to morse

    start_point : str
        The frame to begin inserting keyframes at

    high_val : float
        The high or "on" value to set keyframes to

    low_val : float
        The low or "off" value to set keyframes to

    chosen_property : str
        The property to animate, default is emission strength

    time_unit : int
        The base time unit in frames, equivalent to one dit

    smoothing : int
        The number of frames between high and low points
        Cannot be greater than time_unit
    """

    # Get active object
    obj = bpy.context.active_object

    # Translate plaintext to morse code
    morse = translate(plaintext)

    # Insert keyframes
    insert_keys(obj, morse, start_point, high_val, low_val, chosen_property, time_unit, smoothing)
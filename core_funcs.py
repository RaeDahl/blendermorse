# Main backend functions for morse
# translation and keyframe insertion

# Imports
from includes import *

# Constants
DIT = 1
DAH = 3
LETTERSPACE = 1
WORDSPACE = 5


def insert_keys_emission(obj, morse: str, start_point: int, high: float, low: float, time_unit: int, smoothing: int):
    """
    Description
    ------------
    Keyframes the emission strength of the
    active material
    
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

    time_unit : int
        The base time unit in frames, equivalent to one dit

    smoothing : int
        The number of frames between high and low points
        Cannot be greater than time_unit
    """

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

def insert_keys_light(obj, morse: str, start_point: int, high: float, low: float, time_unit: int, smoothing: int):
        """
    Description
    ------------
    Keyframes the power parameter of a light
    object (point, spot, or area).
    
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

    time_unit : int
        The base time unit in frames, equivalent to one dit

    smoothing : int
        The number of frames between high and low points
        Cannot be greater than time_unit
    """

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

def button_run(plaintext: str, start_point: int, high_val: float, low_val: float, mode: str, time_unit: int, smoothing: int):
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

    mode : str
        The mode to run in, either emission strength of a 
        material or power of a light

    time_unit : int
        The base time unit in frames, equivalent to one dit

    smoothing : int
        The number of frames between high and low points
        Cannot be greater than time_unit
    """

    # Get active object
    obj = bpy.context.active_object

    # Check parameter validity
    if smoothing > time_unit:
        return # TODO: raise error here

    # Translate plaintext to morse code
    morse = translate(plaintext)

    # Insert keyframes
    if mode == "Material":
        insert_keys_emission(obj, morse, start_point, high_val, low_val, time_unit, smoothing)
    elif mode == "Light":
        insert_keys_light(obj, morse, start_point, high_val, low_val, time_unit, smoothing)
    else:
        pass #TODO: raise invalid mode error
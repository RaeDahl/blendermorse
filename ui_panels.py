# GUI menu for blendermorse extension

# Imports
import bpy

# Constants

class BlendermorseGUI(bpy.types.Menu):

    # high value
    high: bpy.props.FloatProperty(
        name = "High Value",
        description = "The high value of the property being set, used for . and -",
        default = 1.0,
        min = 0.0,
        max = None
    )

    # low value
    low: bpy.props.FloatProperty(
        name = "Low Value",
        description = "The low value of the property being set, used for spaces",
        default = 0.0,
        min = 0.0,
        max = None
    )

    # time unit
    time_unit: bpy.props.IntProperty(
        name = "Base Time Unit",
        description = "The base time unit to use, in frames",
        default = 2,
        min = 1,
        max = None
    )

    # smoothing
    smoothing: bpy.props.IntProperty(
        name = "Smoothing",
        description = "Number of frames between high and low value",
        default = 0,
        min = 0,
        max = time_unit # not 100% sure how to make this work
    )

    # start point
    start_point: bpy.props.IntProperty(
        name = "Start Point",
        description = "Frame to start morse code message at",
        default = 0,
        min = 0,
        max = None
    )

    # message
    message: bpy.props.StringProperty(
        name = "Message",
        description = "Plaintext to turn into morse code",
        default = "",
    )

    # chosen property
    chosen_property: # not sure if I want a string or a dropdown
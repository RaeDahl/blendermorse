# GUI menu for blendermorse extension

# Imports
import bpy

# Constants

class BlendermorseGUI(bpy.types.Panel):

    # metadata
    bl_label = "Blendermorse Settings"
    bl_idname = "BlendermorseGUI"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'UI'
    bl_category = 'Morse'

    # TODO: Draw method
    # layout.operator("insert keyframes") # TODO: fix imports + get actual function name

    # inputs

    high = bpy.props.FloatProperty(
        name = "High Value",
        description = "The high value of the property being set, used for . and -",
        default = 1.0,
        min = 0.0,
        max = None
    )

    low = bpy.props.FloatProperty(
        name = "Low Value",
        description = "The low value of the property being set, used for spaces",
        default = 0.0,
        min = 0.0,
        max = None
    )

    time_unit = bpy.props.IntProperty(
        name = "Base Time Unit",
        description = "The base time unit to use, in frames",
        default = 2,
        min = 1,
        max = None
    )

    smoothing = bpy.props.IntProperty(
        name = "Smoothing",
        description = "Number of frames between high and low value",
        default = 0,
        min = 0,
        max = None # May set max to time unit in future versions, for now check on button press
    )

    start_point = bpy.props.IntProperty(
        name = "Start Point",
        description = "Frame to start morse code message at",
        default = 0,
        min = 0,
        max = None
    )

    message = bpy.props.StringProperty(
        name = "Message",
        description = "Plaintext to turn into morse code",
        default = "",
    )

    # mode # light/object material/custom?
    mode = bpy.props.EnumProperty(
        name = "Mode",
        items = [
            ("Material", "Material", "Edit emission strength of material"),
            ("Light", "Light", "Edit the power of a light")
        ]
    )
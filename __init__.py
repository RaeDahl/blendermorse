# main file for running extension

from includes import *

bl_info = {
    "name": "Blendermorse",
    "author": "Rachel Dahl",
    "version": (1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Morse", #TODO: I think this might be wrong but location isn't set in stone yet
    "description": "Blender extension for automatic morse code keyframing",
    "category": "Properties", # TODO: double check this
}

def register():
    bpy.utils.register_class(BlendermorseGUI)
    # TODO: add other classes in same format here

def unregister():
    bpy.utils.register_class(BlendermorseGUI)
    # TODO: add other classes in same format here
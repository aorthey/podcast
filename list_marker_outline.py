bl_info = {
    "name" : "list-marker-outline",
    "author" : "Andreas Orthey",
    "description" : "Iterate over all markers and write an outline to a txt file.",
    "blender" : (4, 0, 0),
    "version" : (1, 0, 0),
    "location": "Sequencer > Marker Menu",
    "category" : "Sequencer"
}

import bpy
import numpy as np
import pathlib

class ListMarkerOutline(bpy.types.Operator):
    """Create an outline from all markers in the sequence editor."""
    bl_idname = "sequencer.list_marker_outline"
    bl_label = "List Marker Outline"
    bl_options = {'REGISTER'}

    def execute(self, context):

        scene = context.scene
        fps = scene.render.fps / scene.render.fps_base

        markers = scene.timeline_markers
        markers = sorted(markers, key=lambda item: item.frame)

        outline_string = "Outline\n"
        for marker in markers:
            frame = marker.frame
            total_seconds=marker.frame/fps
            minutes=int(np.floor(total_seconds/60.0))
            seconds=int(total_seconds-60*minutes)
            outline_string+="{:02d}:{:02d} {}\n".format(minutes,seconds,marker.name)

        blender_file_path = pathlib.Path(bpy.data.filepath)
        if bpy.data.filepath == '':
            print("You are working from an unsaved Blend file. Please save the file first.")
            return

        filename = str(blender_file_path.parent / blender_file_path.stem) + ".txt"
        with open(filename, "w") as text_file:
            text_file.write(outline_string)
        self.report({'INFO'}, "Wrote outline to file {}".format(filename))

        return {'FINISHED'}

def menu_function(self, context):
    self.layout.separator()
    self.layout.operator("sequencer.list_marker_outline")

def register():
    bpy.utils.register_class(ListMarkerOutline)
    bpy.types.SEQUENCER_MT_marker.append(menu_function)

def unregister():
    bpy.utils.unregister_class(ListMarkerOutline)
    bpy.types.SEQUENCER_MT_marker.remove(menu_function)

if __name__ == "__main__":
    register()

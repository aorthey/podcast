bl_info = {
    "name" : "list-marker-outline",
    "author" : "Andreas Orthey",
    "description" : "Iterate over all markers and write an outline.",
    "blender" : (4, 0, 0),
    "version" : (1, 0, 0),
    "location": "Sequencer > Marker Menu",
    "category" : "Generic"
}

import bpy
import numpy as np

scene = bpy.context.scene
fps = scene.render.fps / scene.render.fps_base

markers=bpy.context.scene.timeline_markers
print(markers)

markers = sorted(markers, key=lambda item: item.frame)

for marker in markers:
    frame = marker.frame
    total_seconds=marker.frame/fps
    minutes=int(np.floor(total_seconds/60.0))
    seconds=int(total_seconds-60*minutes)
    print("{:02d}:{:02d} {}".format(minutes,seconds,marker.name))


if __name__ == "__main__":
    register()

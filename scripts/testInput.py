#!/usr/bin/env python
# assume we got a Maya file somewhere as input to this script
file = "/path/to/a/maya/file.ma"
# assume we have a function somewhere that pulls the cameras out of the file
# cameras = getMayaCameras(file)
cameras = ['persp', 'top', 'side', 'bottom', 'camera1']
index = 0
print("Select a camera:")

for c in cameras:
    print("\t(%d) %s" % (index, c))
    index+=1

answer = input("Selection: ")
print("Rendering from camera '" + cameras[int(answer)] + "'.")
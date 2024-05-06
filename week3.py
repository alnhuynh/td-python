# file i/o notes
# fp = open('/tmp/testout', 'w')
# fp.write("1 5 200\n")
# fp.close()

print("Week 3 Homework Exercises")

# 1. take file arg, return list of cameras
def getMayaCameras(filename):
    try:
        with open(filename, 'r') as file:
            cameras = []
            for line in file:
                if line.startswith("createNode camera"):
                    camera_name = line.split('"')[1]
                    cameras.append(camera_name)
        return cameras
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("error reading the file:", e)

cameras = getMayaCameras("\\Users\\sugoi\\Downloads\\example.ma")
print(cameras)

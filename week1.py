import math

print("Week 1 Homework Exercises")

# 1/3b. area of a rectangle
def rectangleArea(length, width):
    if(type(length) != float or type(width) != float):
        return "invalid input"
    elif(length < 0 or width < 0):
        return "invalid input"
    else:
        return length * width

print("1. ", rectangleArea(3.4, 5.6))
print("3b. ", rectangleArea(-2, 5))
print("3b. ", rectangleArea("string", 5))


# 2/3a. area of the circle
def circleArea(radius):
    return math.pi * radius

print("2. ", circleArea(2.56))


# 4. clamp - finds middle value of 3 arguments
def clamp(value, min, max):
    try:
        if(value < min):
            return min
        elif(value > max):
            return max
        else:
            return value
    except TypeError as e:
        print("invalid arguments")

print("exercise 4 tests")
print(clamp(4, 2, 6))
print(clamp(0, 3, 7))
print(clamp(9, 5, 8))
# print(clamp(4, "string", 6))

# 5. padIt - two number argments padded with zeros
def padIt(a, b):
    return f"{a:04.1f}", f"{b:06.2f}"

print("5. ", padIt(3, 4.5))

# 6. getMiddleName from string
def getMiddleName(fullname):
    return fullname.split()[1]

print("6. ", getMiddleName("First Middle Last"))

# 7. getSpheres from list
def getSpheres(list):
    result = []
    for word in list:
        # print(str(word),  " - ", str(word).lower().find("sphere"))
        if str(word).lower().find("sphere") >= 0 :
            result.append(word)
    return result

example = ['nurbsSphere1', 'polyCone1', 'polyCone2', 34, 'dummysPhErE', 'camera1', 'sphere', 'sphere1', '1sphere']
print("7. ", getSpheres(example))
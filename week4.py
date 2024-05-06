# 1. vector script

# 2. rect: corner1, corner2
class Rect:
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2

    def area(self):
        width = abs(self.corner2[0] - self.corner1[0])
        height = abs(self.corner2[1] - self.corner1[1])
        return width * height

    def perimeter(self):
        width = abs(self.corner2[0] - self.corner1[0])
        height = abs(self.corner2[1] - self.corner1[1])
        return (width + height) * 2

    def __str__(self):
        width = abs(self.corner2[0] - self.corner1[0])
        height = abs(self.corner2[1] - self.corner1[1])

        rect_str = ""
        for y in range(height):
            for x in range(width):
                if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                    rect_str += "*"
                else:
                    rect_str += " "
            rect_str += "\n"
        return rect_str

corner1 = (3, 6)
corner2 = (7, -3)
rectangle = Rect(corner1, corner2)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
print("Rectangle:")
print(rectangle)


# 3. rect & square derivation
class Rect:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2


class Square(Rect):
    def __init__(self, width):
        super().__init__(width, width)
        # Rect.__init__(width, length)


rectangle = Rect(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

square = Square(5)
print("\nSquare Area:", square.area())
print("Square Perimeter:", square.perimeter())


# 4. shot and sequence class
class Shot:
    def __init__(self, name, description, length):
        self._name = name
        self._description = description
        self._length = length

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length


class Seq:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._shots = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_shots(self):
        return self._shots

    def add_shot(self, name, description, length):
        new_shot = Shot(name, description, length)
        self._shots.append(new_shot)

    def delete_shot(self, name):
        for shot in self._shots:
            if shot.get_name() == name:
                self._shots.remove(shot)
                break

    def get_seq_length(self):
        total_length = 0
        for shot in self._shots:
            total_length += shot.get_length()
        return total_length


seq = Seq("Sequence 1", "Description of Sequence 1")
seq.add_shot("Shot 1", "Description of Shot 1", 10)
seq.add_shot("Shot 2", "Description of Shot 2", 15)
seq.add_shot("Shot 3", "Description of Shot 3", 20)

print("Sequence Name:", seq.get_name())
print("Sequence Description:", seq.get_description())
print("Sequence Shots:")
for shot in seq.get_shots():
    print("Shot:", shot.get_name(), "Length:", shot.get_length(), "Description:", shot.get_description())

seq.delete_shot("Shot 2")
print("\nAfter deleting Shot 2:")
print("Sequence Shots:")
for shot in seq.get_shots():
    print("Shot:", shot.get_name(), "Length:", shot.get_length(), "Description:", shot.get_description())

print("\nTotal Sequence Length:", seq.get_seq_length())

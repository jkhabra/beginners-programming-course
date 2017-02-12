from string import *


class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

    def __repr__(self):
        return self.__str__()


class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)

    def area(self):
        """
        Returns area of the square
        """
        return self.side**2

    def __str__(self):
        return 'Square with side ' + str(self.side)

    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side


class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)

    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)

    def __str__(self):
        return 'Circle with radius ' + str(self.radius)

    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius


class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: length of base
        height: height of Triangle
        """
        self.base = float(base)
        self.height = float(height)

    def area(self):
        """
        Returns approximate area of the Triangle
        """
        return (self.base * self.height) / 2

    def __str__(self):
        return 'Triangle with base {} and height {}'.format(self.base,
                                                            self.height)

    def __eq__(self, other):
        """
        Two Triangle are equal if they have same base and height
        other: object to check for equality
        """
        return type(other) == Triangle \
            and self.base == other.base \
            and self.height == other.height


class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.shapes_list = []

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if sh not in self.shapes_list:
            self.shapes_list.append(sh)

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        for i in self.shapes_list:
            yield i

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        each_shpe = ''
        for i in self.shapes_list:
            each_shpe += str(i) + '\n'

        return each_shpe.strip()

    def __len__(self):
        return len(self.shapes_list)

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for i in self:
            if i not in other:
                return False

        return True


def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the largest area
    """
    biggest = None
    result = ()
    for i in shapes:
        if not biggest:
            biggest = i

        if i.area() > biggest.area():
            biggest = i

    for i in shapes:
        if i.area() == biggest.area():
            result += (i,)

    return result


def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    """
    set_shapes = ShapeSet()
    with open(filename, 'r') as foo:
        for line in foo:
            shape_checker = line.split(',')
            if shape_checker[0] == 'circle':
                sh = Circle(shape_checker[1])

            if shape_checker[0] == 'square':
                sh = Square(shape_checker[1])

            if shape_checker[0] == 'triangle':
                sh = Triangle(shape_checker[1], shape_checker[-1])

            set_shapes.addShape(sh)

        return set_shapes


if __name__ == '__main__':
    ss = ShapeSet()

    ss.addShape(Triangle(3, 8))
    ss.addShape(Circle(1))
    ss.addShape(Triangle(4, 6))
    largest = findLargest(ss)
    for e in largest:
        print(e)

    ss.addShape(Triangle(1.2, 2.5))
    ss.addShape(Circle(4))
    ss.addShape(Square(3.6))
    ss.addShape(Triangle(1.6, 6.4))
    ss.addShape(Circle(2.2))
    largest = findLargest(ss)
    for e in largest:
        print(e)

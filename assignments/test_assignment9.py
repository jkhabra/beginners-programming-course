from assignment9 import (Square, Circle, Triangle,
                         ShapeSet, findLargest,
                         readShapesFromFile)


class TestTriangle:
    def setup(self):
        self.t1 = Triangle(12, 12)
        self.t2 = Triangle(10, 12)
        self.t3 = Triangle(12, 13)
        self.t4 = Triangle(10, 12)

    def test_area(self):
        assert self.t1.area() == 72
        assert self.t2.area() == 60
        assert self.t3.area() == 78

    def test_str(self):
        assert str(self.t1) == "Triangle with base 12.0 and height 12.0"
        assert str(self.t2) == "Triangle with base 10.0 and height 12.0"
        assert str(self.t3) == "Triangle with base 12.0 and height 13.0"

    def test_eq(self):
        assert (self.t1 == self.t2) is False
        assert (self.t2 == self.t3) is False
        assert (self.t2 == self.t4) is True


def test_findLargest():
    ss = ShapeSet()
    t1 = Triangle(3, 8)
    t2 = Triangle(4, 6)
    c1 = Circle(1)

    ss.addShape(t1)
    ss.addShape(t2)
    ss.addShape(c1)

    largest = findLargest(ss)

    for i in largest:
        assert t1 in largest and t2 in largest


class TestShapeSet():
    def setup(self):
        self.sh = ShapeSet()
        self.sh1 = ShapeSet()
        self.t1 = Triangle(2, 6)
        self.t2 = Triangle(9, 3)
        self.t3 = Square(9)
        self.t4 = Circle(8)

        self.sh.addShape(self.t1)
        self.sh.addShape(self.t2)
        self.sh.addShape(self.t3)
        self.sh1.addShape(self.t1)
        self.l = [self.t1, self.t2, self.t3]

    def test_addShape(self):
        assert self.t1 in self.sh
        assert self.t2 in self.sh
        assert self.t3 in self.sh
        assert self.t4 not in self.sh

    def test_iter(self):
        iter(self.sh)
        for (v, i) in enumerate(self.sh):
            assert i == self.l[v]

    def test_str(self):
        assert str(self.sh1) == 'Triangle with base 2.0 and height 6.0'

    def test_eq(self):
        assert (self.sh == self.sh1) is False

    def test_len(self):
        assert len(self.sh) == 3
        assert len(self.sh1) == 1

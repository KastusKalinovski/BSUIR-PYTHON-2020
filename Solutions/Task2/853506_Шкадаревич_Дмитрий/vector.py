import math


class VectorError(Exception):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        if self.message != "":
            return self.message
        else:
            return "VectorError has been raised"


class Vector:
    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
            self.dimension = 2
        else:
            self.values = args
            self.dimension = len(self.values)

    def norm(self):
        """ Returns the norm of the vector"""
        return math.sqrt(sum(x ** 2 for x in self.values))

    def normalize(self):
        """ Returns a normalized unit vector """
        norm = self.norm()
        return Vector(*(x / norm for x in self.values))

    def inner(self, other):
        """ Returns the dot product (inner product) of self and other vector"""
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if type(other) == type(self):
            return self.inner(other)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple(a * other for a in self)
            return Vector(*product)

    def __add__(self, other):
        if self.dimension == other.dimension:
            new_vector = []
            for a, b in zip(self.values, other.values):
                new_vector.append(a + b)
            return Vector(*new_vector)
        else:
            raise VectorError("The dimension of the vectors is not equal")

    def __sub__(self, other):
        if self.dimension == other.dimension:
            new_vector = []
            for a, b in zip(self.values, other.values):
                new_vector.append(a - b)
            return Vector(*new_vector)
        else:
            raise VectorError("The dimension of the vectors is not equal")

    def __eq__(self, other):
        if self.dimension == other.dimension:
            equal = False
            for a, b in zip(self.values, other.values):
                if a != b:
                    break
            else:
                equal = True
            return equal
        else:
            raise VectorError("The dimension of the vectors is not equal")

    def __repr__(self):
        return "Vector ({})".format(", ".join(str(x) for x in self.values))

    def __str__(self):
        return "Vector ({})".format(", ".join(str(x) for x in self.values))

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]


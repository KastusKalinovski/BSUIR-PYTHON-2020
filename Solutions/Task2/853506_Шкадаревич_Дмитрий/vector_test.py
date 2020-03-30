import unittest
from vector import Vector, VectorError
from numpy import linalg as LA


class CacheTestCase(unittest.TestCase):

    def test_norm(self):
        a = Vector(1, 2, 3, 4, 5)
        self.assertEqual(a.norm(), LA.norm(a))

    def test_sum(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(a + b, Vector(3, 5, 7))

    def test_sub(self):
        a = Vector(3, 3, 4)
        b = Vector(2, 3, 4)
        self.assertEqual(a - b, Vector(1, 0, 0))

    def test_mul_num(self):
        a = Vector(3, 3, 4)
        self.assertEqual(a * 2, Vector(6, 6, 8))

    def test_dot_product(self):
        a = Vector(1, 1, 1)
        b = Vector(2, 2, 4)
        self.assertEqual(a * b, 8)

    def test_size(self):
        a = Vector(1, 2, 3, 4, 5, 6)
        self.assertEqual(len(a), 6)

    def test_equal(self):
        a = Vector(1, 1, 1)
        b = Vector(1, 2, 3)
        c = Vector(1, 1, 1)

        self.assertEqual(a == b, False)
        self.assertEqual(a == c, True)

    def test_index(self):
        a = Vector(32, 10, 50)
        self.assertEqual(a[1], 10)


unittest.main()

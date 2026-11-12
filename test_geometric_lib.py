import unittest
import math
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = circle.area(5)
        self.assertAlmostEqual(res, math.pi * 25)

    def test_area_float(self):
        res = circle.area(2.5)
        self.assertAlmostEqual(res, math.pi * 6.25)

    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = circle.perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_area_normal(self):
        res = rectangle.area(5, 7)
        self.assertEqual(res, 35)

    def test_perimeter_zero(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = rectangle.perimeter(5, 7)
        self.assertEqual(res, 24)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_area_float(self):
        res = square.area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_positive(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = triangle.area(6, 4)
        self.assertEqual(res, 12)

    def test_area_float(self):
        res = triangle.area(5, 3)
        self.assertAlmostEqual(res, 7.5)

    def test_perimeter_zero(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)


if __name__ == '__main__':
    unittest.main()
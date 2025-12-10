import unittest
import math
import rectangle
import square
import circle
import triangle


class TestRectangle(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(rectangle.area(5, 10), 50)
        self.assertEqual(rectangle.area(0, 10), 0)
        self.assertEqual(rectangle.area(2.5, 4), 10.0)
    
    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)
        self.assertEqual(rectangle.perimeter(0, 10), 20)
        self.assertEqual(rectangle.perimeter(2.5, 3.5), 12.0)
    
    def test_negative_value(self):
        self.assertFalse(rectangle.perimeter(-1, 2))
        self.assertFalse(rectangle.perimeter(-10, -5))
        self.assertFalse(rectangle.area(-1, 2))
        self.assertFalse(rectangle.area(-10, -5))


class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(circle.area(10), math.pi*10*10)
        self.assertAlmostEqual(circle.area(math.pi), math.pi**3)
        self.assertAlmostEqual(circle.area(0), 0)
    
    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(10), 2*math.pi*10)
        self.assertAlmostEqual(circle.perimeter(math.pi), 2*math.pi**2)
        self.assertAlmostEqual(circle.perimeter(0), 0)
    
    def test_negative_value(self):
        self.assertFalse(circle.area(-5))
        self.assertFalse(circle.perimeter(-math.pi))


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(2.5), 2.5*2.5)
    
    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(2.5), 2.5*4)
    
    def test_negative_value(self):
        self.assertFalse(square.perimeter(-1))
        self.assertFalse(square.area(-10))

class TestTriangle(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(triangle.area(5, 10), 25)
        self.assertEqual(triangle.area(0, 10), 0)
        self.assertEqual(triangle.area(2.5, 4), 5)
    
    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 10, 7), 22)
        self.assertEqual(triangle.perimeter(0, 10, 12), 0)
        self.assertEqual(triangle.perimeter(2.5, 4, 3), 9.5)
    
    def test_negative_value(self):
        self.assertFalse(triangle.perimeter(-1, 2, 3))
        self.assertFalse(triangle.area(-1, 2))
    
    def triangle_does_not_exist(self):
        self.assertFalse(triangle.perimeter(10, 1, 2))
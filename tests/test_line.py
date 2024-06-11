# test class for Line class

import unittest

from app.line import Line
from app.point import Point

class TestLine(unittest.TestCase):
    def setUp(self):
        pass
    
    # also tests Point getters
    def test_init(self):
        p1 = Point(0.0, 1.0)
        p2 = Point(1.0, 0.0)
        L = Line(p1, p2)
        self.assertEqual(L.get_p1(), p1)
        self.assertEqual(L.get_p2(), p2)
        
    def test_init_exception(self):
        with self.assertRaises(ValueError) as context_manager:
            # TBD change this if we implement a tuple initializer for Point
            Line(Point(0.0, 1.0), (2.0, 3.0))
        self.assertEquals(type(context_manager.exception), ValueError)
        
    def test_repr(self):
        p1 = Point(0.0, 1.0)
        p2 = Point(1.0, 0.0)        
        L = Line(p1, p2)
        self.assertEquals(repr(L), "_(0.0,1.0),(1.0,0.0)_")
        
    def test_set_p1(self):
        p1 = Point(0.0, 1.0)
        p2 = Point(1.0, 0.0)        
        L = Line(p1, p2)
        p3 = Point(1.2, 3.4)
        L.set_p1(p3)
        self.assertEquals(L.get_p1(), p3)
        self.assertEquals(L.get_p2(), p2)
        
    def test_set_p2(self):
        p1 = Point(0.0, 1.0)
        p2 = Point(1.0, 0.0)        
        L = Line(p1, p2)
        p3 = Point(1.2, 3.4)
        L.set_p2(p3)
        self.assertEquals(L.get_p1(), p1)
        self.assertEquals(L.get_p2(), p3)
        
    def test_set_p1_exception(self):
        p1 = Point(0.0, 1.0)
        p2 = Point(1.0, 0.0)        
        L = Line(p1, p2)
        with self.assertRaises(ValueError) as context_manager:
            L.set_p1(None)
        self.assertEquals(type(context_manager.exception), ValueError)
        
    def test_get_line_points(self):
        p1 = Point(0.0, 1.0)
        p2 = Point(1.0, 0.0)        
        L = Line(p1, p2)
        rv = L.get_line_points()
        self.assertEquals(rv, (p1, p2))
        self.assertEquals(type(rv), tuple)
        self.assertEquals(type(rv[0]), Point)
        self.assertEquals(type(rv[1]), Point)
        
    def test_get_line_raw(self):
        p1 = Point(0.0, 1.0)
        p2 = Point(1.0, 0.0)        
        L = Line(p1, p2)
        rv = L.get_line_raw()
        self.assertEquals(rv, ((0.0, 1.0), (1.0, 0.0)))
        self.assertEquals(type(rv), tuple)
        
    def test_get_length(self):
        # pythagorean triplet: 3,4,5
        p1 = Point(0.0, 0.0)
        p2 = Point(3.0, 4.0)
        L = Line(p1, p2)
        self.assertEquals(L.get_length(), 5.0)
        
    def test_get_slope(self):
        p1 = Point(0.0, 2.0)
        p2 = Point(1.0, 0.0)        
        L = Line(p1, p2)
        self.assertEquals(L.get_slope(), -2.0)
        
    def test_get_slope_vertical(self):
        p1 = Point(1.0, 2.0)
        p2 = Point(1.0, 0.0)        
        L = Line(p1, p2)
        self.assertEquals(L.get_slope(), 'undef')
        
    def test_get_intercept(self):
        # y = 5x + 9
        p1 = Point(0.0, 9.0)
        p2 = Point(1.0, 14.0)
        L = Line(p1, p2)
        self.assertEquals(L.get_intercept(), 9.0)
        
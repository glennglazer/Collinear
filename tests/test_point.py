# test class for Point class

import unittest

from app.point import Point

class TestPoint(unittest.TestCase):
    def setUp(self):
        pass
    
    # also tests getters
    def test_init(self):
        p = Point(1.2, 3.4)
        self.assertEqual(p.get_x(), 1.2)
        self.assertEqual(p.get_y(), 3.4)
        
    def test_init_exception(self):
        with self.assertRaises(ValueError) as context_manager:
            Point(x=1.0)
        self.assertEquals(type(context_manager.exception), ValueError)
    
    def test_repr(self):
        p = Point(1.2, 3.4)
        self.assertEquals(repr(p), "(1.2,3.4)")
        
    def test_set_x(self):
        p = Point(1.2, 3.4)
        p.set_x(3.141)
        self.assertEquals(p.get_x(), 3.141)
        self.assertEquals(p.get_y(), 3.4)
        
    def test_set_y(self):
        p = Point(1.2, 3.4)
        p.set_y(2.717)
        self.assertEquals(p.get_x(), 1.2)
        self.assertEquals(p.get_y(), 2.717)
        
    def test_set_x_exception(self):
        p = Point(1.2, 3.4)
        with self.assertRaises(ValueError) as context_manager:
            p.set_x('NaN')
        self.assertEquals(type(context_manager.exception), ValueError)        
        
    def test_get_point(self):
        p = Point(1.2, 3.4)
        rv = p.get_point()
        self.assertEquals(rv, (1.2, 3.4))
        self.assertEquals(type(rv), tuple)
        
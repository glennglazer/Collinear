# test class for collinear class

import unittest

from app.collinear import Collinear
from app.line import Line
from app.point import Point

class TestCollinear(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_init_exception(self):
        with self.assertRaises(AttributeError) as context_manager:
            Collinear()
        self.assertEquals(type(context_manager.exception), AttributeError)
        
    def test_is_collinear_geometric_shortcut(self):
        L1 = Line(Point(1.0, 1.0), Point(2.0, 2.0))
        L2 = Line(Point(2.0, 2.0), Point(3.0, 3.0))
        C = Collinear(L1, L2)
        self.assertTrue(C.is_collinear_geometric())
        
    def test_is_collinear_geometric(self):
        L1 = Line(Point(1.0, 1.0), Point(2.0, 2.0))
        L2 = Line(Point(4.0, 4.0), Point(5.0, 5.0))
        C = Collinear(L1, L2)
        self.assertTrue(C.is_collinear_geometric())
        
    def test_is_not_collinear_geometric_different_slopes(self):
        L1 = Line(Point(1.0, 12.0), Point(2.0, 2.0))
        L2 = Line(Point(4.0, 4.0), Point(5.0, 5.0))
        C = Collinear(L1, L2)
        self.assertFalse(C.is_collinear_geometric())
        
    def test_is_not_collinear_geometric_different_intercepts(self):
        L1 = Line(Point(1.0, 3.0), Point(2.0, 4.0))
        L2 = Line(Point(4.0, 4.0), Point(5.0, 5.0))
        C = Collinear(L1, L2)
        self.assertFalse(C.is_collinear_geometric())
        
    def test_is_collinear_dot_product(self):
        L1 = Line(Point(1.0, 1.0), Point(2.0, 2.0))
        L2 = Line(Point(2.0, 2.0), Point(3.0, 3.0))
        C = Collinear(L1, L2)
        self.assertTrue(C.is_collinear_dot_product())
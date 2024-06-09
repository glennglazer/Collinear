# determine if two line segments are collinear
# using numpy is "cheating"

from app.line import Line
from math import isclose


import logging

logger = logging.getLogger(__file__)

class Collinear():
    def __init__(self, L1: Line = None, L2: Line = None) -> None:
        if L1 is None or L2 is None or type(L1) is not Line or type(L2) is not Line:
            raise ValueError(f"Both p1 {self.L1} and p2 {self.L2} must both be specified as Lines")
        self.L1 = L1
        self.L2 = L2        
    
    def is_collinear_geometric(self) -> bool:
        m1 = self.L1.get_slope()
        m2 = self.L2.get_slope()
        if m1 != m2:
            logger.error(f"{self.L1} and {self.L2} have different slopes ({m1} and {m2} respectively)")
            return False
        
        # shortcut if they have a middle point in common
        # AB, BC or AB, AC
        # this derives from the uniqueness (up to representation) of the slope-intercept form: if a point on a line satisfies the equation, all of them do
        if self.L1.get_p1() in [self.L2.get_p1(), self.L2.get_p2()]:
            return True
        
        intercept1 = self.L1.get_intercept()
        intercept2 = self.L2.get_intercept()
        if intercept1 == intercept2:
            return True
        else:
            logger.error(f"{self.L1} and {self.L2} have different intercepts ({intercept1} and {intercept2} respectively)")
            
    def is_collinear_dot_product(self) -> bool:
        # (B.x-A.x)*(D.x-C.x) + (B.y-A.y)*(D.y-C.y)
        L1_delta_x = self.L1.get_p2().get_x() - self.L1.get_p1().get_x()
        L1_delta_y = self.L1.get_p2().get_y() - self.L1.get_p1().get_y()
        L2_delta_x = self.L2.get_p2().get_x() - self.L2.get_p1().get_x()
        L2_delta_y = self.L2.get_p2().get_y() - self.L2.get_p1().get_y()
        dot = (L1_delta_x * L2_delta_x) + (L1_delta_y * L2_delta_y)
        # the other way would be to normalize the vectors first, this seems faster
        normalized_dot = dot / (self.L1.get_length() * self.L2.get_length())
        # isclose covers floating point "equality"
        if isclose(normalized_dot, 1):
            return True
        else:
            logger.error(f"Normalized dot product of {self.L1} and {self.L2} is not 1, it is {normalized_dot}")
        
# class to encapsulate a line in $\mathbb{R}^ 2$ as an abstract object. No graphics drawing intended.

from app.point import Point
# ^ operator doesn't like floats
from math import pow, sqrt

class Line:
    def __init__(self, p1: Point = None, p2: Point = None) -> None:
        if p1 is None or p2 is None or type(p1) is not Point or type(p2) is not Point:
            raise ValueError(f"Both p1 {p1} and p2 {p2} must both be specified as Points")
        self.p1 = p1
        self.p2 = p2
        
    def __repr__(self) -> str:
        return (f"_{repr(self.p1)},{repr(self.p2)}_")
    
    def get_p1(self) -> Point:
        return self.p1
    
    def get_p2(self) -> Point:
        return self.p2
    
    def get_line_points(self) -> tuple:
        return (self.p1, self.p2)
    
    def get_line_raw(self) -> tuple[tuple, tuple]:
        return (self.p1.get_point(), self.p2.get_point())
    
    def get_length(self) -> float:
        # h/t Pythagoras
        delta_x = pow((self.p1.get_x() - self.p2.get_x()), 2)
        delta_y = pow((self.p1.get_y() - self.p2.get_y()), 2)
        return sqrt(delta_x + delta_y)
    
    def get_slope(self) -> float | str:
        delta_x = (self.p2.get_x() - self.p1.get_x())
        if delta_x == 0:
            # vertical line, slope undefined
            # for the purposes of colinearity, we just need the slope to be the same
            return "undef"
        delta_y = (self.p2.get_y() - self.p1.get_y())
        return delta_y / delta_x
    
    def get_intercept(self) -> float:
        #  b = m (0 - x1) + y1
        m = self.get_slope()
        return m * (0.0 - self.p1.get_x()) + self.p1.get_y()
    
    def set_p1(self, p1: Point = None) -> None:
        if p1 is None or type(p1) is not Point:
            raise ValueError(f"p1 {p1} must be specified as a Point")
        self.p1 = p1
        
    def set_p2(self, p2: Point = None) -> None:
        if p2 is None or type(p2) is not Point:
            raise ValueError(f"p2 {p2} must be specified as a Point")
        self.p2 = p2
        
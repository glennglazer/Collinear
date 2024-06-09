# class to encapsulate a point in $\mathbb{R}^ 2$

class Point:
    def __init__(self, x: float = None, y: float = None) -> None:
        if x is None or y is None or type(x) is not float or type(y) is not float:
            raise ValueError(f"Both x {x} and y {y} must both be specified as floats")
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return (f"({self.x},{self.y})")
    
    def get_x(self) -> float:
        return self.x
    
    def get_y(self) -> float:
        return self.y
    
    def get_point(self) -> tuple:
        return (self.x, self.y)
    
    def set_x(self, x: float = None) -> None:
        if x is None or type(x) is not float:
            raise ValueError(f"x {x} must be specified as a float")
        self.x = x
        
    def set_y(self, y: float = None) -> None:
        if y is None or type(y) is not float:
            raise ValueError(f"y {y} must be specified as a float")
        self.y = y   
    
    
from point import *
class Cell:
    def __init__(self, canvas):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = canvas
        
    def draw(self, point1, point2):
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        if self.has_left_wall:
            p1 = point1
            p2 = Point(self._x1, self._y2)
            Line(p1, p2).draw(self._win, 'black')
        if self.has_right_wall:
            p1 = point2
            p2 = Point(self._x2, self._y1)
            Line(p1, p2).draw(self._win, 'black')
        if self.has_top_wall:
            p1 = point1
            p2 = Point(self._x2, self._y1)
            Line(p1, p2).draw(self._win, 'black')
        if self.has_bottom_wall:
            p1 = point2
            p2 = Point(self._x1, self._y2)
            Line(p1, p2).draw(self._win, 'black')
                
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
        self.visited = False
        self._win = canvas
        
    def draw(self, point1, point2):
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        top_left = point1
        top_right = Point(self._x2, self._y1)
        bot_left = Point(self._x1, self._y2)
        bot_right = point2 
        if self.has_left_wall:
            Line(top_left, bot_left).draw(self._win, 'black')
        else:
            Line(top_left, bot_left).draw(self._win, 'white')
        if self.has_right_wall:
            Line(top_right, bot_right).draw(self._win, 'black')
        else:
            Line(top_right, bot_right).draw(self._win, 'white')
        if self.has_top_wall:
            Line(top_left, top_right).draw(self._win, 'black')
        else:
            Line(top_left, top_right).draw(self._win, 'white')
        if self.has_bottom_wall:
            Line(bot_left, bot_right).draw(self._win, 'black')
        else:
            Line(bot_left, bot_right).draw(self._win, 'white')
    def cell_move(self, to_cell, undo=False):
        color = 'red'
        if undo:
            color = 'gray'
        center1 = Point((self._x2+self._x1)/2, (self._y2+self._y1)/2)
        print(center1)
        center2 = Point((to_cell._x2+to_cell._x1)/2, (to_cell._y2+to_cell._y1)/2)
        print(center2)
        Line(center1, center2).draw(self._win, color)
        
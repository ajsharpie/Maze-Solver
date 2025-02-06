from window import Window
from point import *
from cell import Cell
import random
def main():
    win = Window(800, 600)
    p1 = Point(2,2)
    p2 = Point(50,50)
    p3 = Point(50,2)
    p4 = Point(100, 50)
    c1 = Cell(win.canvas)
    c1.draw(p1, p2)
    c2 = Cell(win.canvas)
    c2.draw(p3, p4)
    c1.cell_move(c2)
    
    win.wait_for_close()

def make_point(range_low, range_high):
    x = random.randrange(range_low, range_high)
    y = random.randrange(range_low, range_high)
    return Point(x, y)

if __name__=='__main__':
    main()
from window import Window
from point import *
from cell import Cell
def main():
    win = Window(800, 600)
    p1 = Point(2, 2)
    p2 = Point(50, 50)
    cell = Cell(win.canvas).draw(p1, p2)
    win.wait_for_close()


if __name__=='__main__':
    main()
from window import Window
from point import *
def main():
    win = Window(800, 600)
    p1 = Point(122, 122)
    p2 = Point(222, 222)
    p3 = Point(0, 0)
    p4 = Point(122, 222)
    l1 = Line(p1, p2)
    l2 = Line(p3, p4)
    win.draw_line(l1, 'black')
    win.draw_line(l2, 'red')
    win.wait_for_close()


if __name__=='__main__':
    main()
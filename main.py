from window import Window
from point import *
from maze import Maze
import random
def main():
    win = Window(800, 600)
    win.canvas.configure(background='white')
    #--render from here down to bottom--
    
    num_cols = 15
    num_rows = 15
    m1 = Maze(2, 2, num_rows, num_cols, 15, 15, win=win, seed=1)
    
    
    
    #--bottom of render code--
    win.wait_for_close()

def make_point(range_low, range_high):
    x = random.randrange(range_low, range_high)
    y = random.randrange(range_low, range_high)
    return Point(x, y)

if __name__=='__main__':
    main()
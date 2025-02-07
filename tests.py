import unittest
from maze import Maze
from window import Window
import random

class Tests(unittest.TestCase):
    mywin = Window(800, 600)
    
    def test_maze_create_cells(self):
        num_cols = 18
        num_rows = 13
        m1 = Maze(2, 2, num_rows, num_cols, 20, 20, win=Tests.mywin)
        
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        
        self.assertEqual(
            len(m1._cells[0]), 
            num_rows
        )
    
    def test_maze_reset_visited(self):
        num_cols = 18
        num_rows = 13
        m1 = Maze(2, 2, num_rows, num_cols, 20, 20, win=Tests.mywin)
        
        self.assertFalse(
            m1._cells[random.randrange(0, num_cols)][random.randrange(0, num_rows)].visited
        )
    
if __name__=='__main__':
    unittest.main()
from cell import Cell
from point import Point
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed != None:
            self.seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited(0, 0)
        
    def _create_cells(self):
        self._cells = [[Cell(self.win.canvas) for i in range(self.num_rows)] for i in range(self.num_cols)]
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)
    
    def _draw_cell(self, i, j):
        size_offsetx = self.cell_size_x
        size_offsety = self.cell_size_y
        x1 = i*(size_offsetx)+self.x1
        y1 = j*(size_offsety)+self.y1
        x2 = x1+size_offsetx
        y2 = y1+size_offsety        
        cell = self._cells[i][j]
        cell.draw(Point(x1, y1), Point(x2, y2))
        self._animate()
        
    def _animate(self):
        self.win.redraw()
        time.sleep(.001)
    
    def _break_entrance_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0,0)
        last_col = len(self._cells)-1
        last_row = len(self._cells[last_col])-1
        self._cells[last_col][last_row].has_right_wall = False
        self._draw_cell(last_col, last_row)
    
    def _break_walls_r(self, i, j):
        cells = self._cells
        cells[i][j].visited = True
        while True:
            to_visit = []
            directions = []
            if i+1 < len(cells):
                if cells[i+1][j].visited == False:
                    to_visit.append(cells[i+1][j])
                    directions.append('right')
            if j+1 < len(cells[i]):
                if cells[i][j+1].visited == False:
                    to_visit.append(cells[i][j+1])
                    directions.append('down')
            if i-1 >= 0:
                if cells[i-1][j].visited == False:
                    to_visit.append(cells[i-1][j])
                    directions.append('left')
            if j-1 >= 0:
                if cells[i][j-1].visited == False:
                    to_visit.append(cells[i][j-1])
                    directions.append('up')
            
            if directions == []:
                self._draw_cell(i, j)
                return
            
            direction = directions[random.randrange(0, len(directions))]
            cell = self._cells[i][j]
            match direction:
                case 'right':
                    cell.has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                    self._cells[i+1][j].visited = True
                    to_visit.remove(self._cells[i+1][j])
                    self._draw_cell(i, j)
                    self._draw_cell(i+1, j)
                    self._break_walls_r(i+1, j)
                case 'left':
                    cell.has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                    self._cells[i-1][j].visited = True
                    to_visit.remove(self._cells[i-1][j])
                    self._draw_cell(i, j)
                    self._draw_cell(i-1, j)
                    self._break_walls_r(i-1, j)
                case 'up':
                    cell.has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                    self._cells[i][j-1].visited = True
                    to_visit.remove(self._cells[i][j-1])
                    self._draw_cell(i, j)
                    self._draw_cell(i, j-1)
                    self._break_walls_r(i, j-1)
                case 'down':
                    cell.has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                    self._cells[i][j+1].visited = True
                    to_visit.remove(self._cells[i][j+1])
                    self._draw_cell(i, j)
                    self._draw_cell(i, j+1)
                    self._break_walls_r(i, j+1)
            if to_visit == []:
                return

                
        
        # to_visit = []
        # visited = []
        
        # for i in self._cells:
        #     to_visit.append(i)
        #     while to_visit != []:
        #         row = to_visit.pop(0)
        #         for cell in row:
                    
    def _reset_cells_visited(self, i, j):
        cells = self._cells
        cells[i][j].visited = True
        while True:
            to_visit = []
            directions = []
            if i+1 < len(cells):
                if cells[i+1][j].visited == True:
                    to_visit.append(cells[i+1][j])
                    directions.append('right')
            if j+1 < len(cells[i]):
                if cells[i][j+1].visited == True:
                    to_visit.append(cells[i][j+1])
                    directions.append('down')
            if i-1 > 0:
                if cells[i-1][j].visited == True:
                    to_visit.append(cells[i-1][j])
                    directions.append('left')
            if j-1 > 0:
                if cells[i][j-1].visited == True:
                    to_visit.append(cells[i][j-1])
                    directions.append('up')
            
            if directions == []:
                self._draw_cell(i, j)
                return
            
            direction = directions[random.randrange(0, len(directions))]
            cell = self._cells[i][j]
            match direction:
                case 'right':
                    cell.vistited = False
                    self._cells[i+1][j].visited = False
                    to_visit.remove(self._cells[i+1][j])
                case 'left':
                    cell.visited = False
                    self._cells[i-1][j].visited = False
                    to_visit.remove(self._cells[i-1][j])
                case 'up':
                    cell.visited = False
                    self._cells[i][j-1].visited = False
                    to_visit.remove(self._cells[i][j-1])
                case 'down':
                    cell.visited = False
                    self._cells[i][j+1].visited = False
                    to_visit.remove(self._cells[i][j+1])
            if to_visit == []:
                return
from tkinter import Tk, BOTH, Canvas
from point import Line

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tk_root = Tk()
        self.tk_root.title = 'main window'
        self.canvas = Canvas()
        self.canvas.pack()
        self.is_running = False
        self.tk_root.protocol('WM_DELETE_WINDOW', self.close)
        
        
    def redraw(self):
        self.tk_root.update_idletasks()
        self.tk_root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False
        
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        
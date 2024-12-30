from tkinter import Tk, BOTH, Canvas

from shapes import Line
class Window:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title("maze")
        self.canvas = Canvas(self.root_widget, width=width, height=height)
        self.canvas.pack()
        self.is_win_running = False

        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.is_win_running = True
        while self.is_win_running:
            self.redraw()
        
    
    def close(self):
        self.is_win_running = False

    def draw_line(self, line: Line, fillColor):
        line.draw(self.canvas, fillColor)
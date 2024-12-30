from window import Window
from shapes import Line, Point
from  units import Cell
from maze import Maze

def cellDrawAndMoveTest():
    win = Window(800, 600)
    all_sides_closed = Cell(win)

    left_open = Cell(win)
    left_open.has_left_wall = False

    right_open = Cell(win)
    right_open.has_right_wall = False

    top_open = Cell(win)
    top_open.has_top_wall = False

    bottom_open = Cell(win)
    bottom_open.has_bottom_wall = False

    all_sides_closed.draw(10,20,30,40)
    
    right_open.draw(10,80,30,100)
    left_open.draw(40,80,60,100)
    right_open.draw_move(left_open, True)

    bottom_open.draw(10,110,30,130)
    top_open.draw(10,140,30,160)

    bottom_open.draw_move(top_open)

    win.wait_for_close()

def maze_draw_test():
    win = Window(800, 600)
    
    maze = Maze(50,100, 5, 10, 10,20,win)
    
    win.wait_for_close()

if __name__ == "__main__":
    maze_draw_test()
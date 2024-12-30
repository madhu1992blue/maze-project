from shapes import Point, Line
from window import Window
from typing import Optional

class Cell:
    def __init__(self,
        win: Optional[Window] = None
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.top_left: Point = Point(0,0)
        self.bottom_right: Point = Point(0,0)
        self.win: Optional[Window] = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.top_left = Point(x1,y1)
        self.bottom_right = Point(x2, y2)

        if self.has_left_wall:
            left_wall_color = "black"
        else: 
            left_wall_color = "#d9d9d9"
        left_wall_top = self.top_left
        left_wall_bottom = Point(self.top_left.x, self.bottom_right.y)
        
        if self.has_right_wall:
            right_wall_color = "black"
        else:
            right_wall_color = "#d9d9d9"
        right_wall_top = Point(self.bottom_right.x, self.top_left.y)
        right_wall_bottom = self.bottom_right
      
        if self.has_top_wall:
            top_wall_color = "black"
        else:
            top_wall_color ="#d9d9d9"
        top_wall_left = self.top_left
        top_wall_right = Point(self.bottom_right.x, self.top_left.y)
      
            
        if self.has_bottom_wall:
            bottom_wall_color = "black"
        else:
            bottom_wall_color = "#d9d9d9"
        bottom_wall_left = Point(self.top_left.x,self.bottom_right.y)
        bottom_wall_right = self.bottom_right
        
        if self.win:
            self.win.draw_line(Line(left_wall_top, left_wall_bottom),left_wall_color)
            self.win.draw_line(Line(right_wall_top, right_wall_bottom),right_wall_color)
            self.win.draw_line(Line(top_wall_left, top_wall_right),top_wall_color)
            self.win.draw_line(Line(bottom_wall_left, bottom_wall_right),bottom_wall_color)
    
    def draw_move(self, to_cell, undo=False):
        current_cell_center = Point(
                                (self.top_left.x + self.bottom_right.x)//2,
                                (self.top_left.y+self.bottom_right.y) //2
                                )
        to_cell_center = Point(
                                (to_cell.top_left.x + to_cell.bottom_right.x)//2,
                                (to_cell.top_left.y+to_cell.bottom_right.y) //2
                                )
        if not undo:
            color = "red"
        else:
            color = "gray"
        if self.win:
            self.win.draw_line(
                Line(current_cell_center, to_cell_center),
                color
            )


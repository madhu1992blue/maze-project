from shapes import Point, Line
from window import Window

class Cell:
    def __init__(self,
        win: Window
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__top_left: Point = Point(0,0)
        self.__bottom_right: Point = Point(0,0)
        self.win = win

    def draw(self, x1, y1, x2, y2):
        self.__top_left = Point(x1,y1)
        self.__bottom_right = Point(x2, y2)
        if self.has_left_wall:
            left_wall_top = self.__top_left
            left_wall_bottom = Point(self.__top_left.x, self.__bottom_right.y)
            self.win.draw_line(Line(left_wall_top, left_wall_bottom),"red")
        if self.has_right_wall:
            right_wall_top = Point(self.__bottom_right.x, self.__top_left.y)
            right_wall_bottom = self.__bottom_right
            self.win.draw_line(Line(right_wall_top, right_wall_bottom),"red")
        if self.has_top_wall:
            top_wall_left = self.__top_left
            top_wall_right = Point(self.__bottom_right.x, self.__top_left.y)
            self.win.draw_line(Line(top_wall_left, top_wall_right),"red")
        if self.has_bottom_wall:
            bottom_wall_left = Point(self.__top_left.x,self.__bottom_right.y)
            bottom_wall_right = self.__bottom_right
            self.win.draw_line(Line(bottom_wall_left, bottom_wall_right),"red")
    
    def draw_move(self, to_cell, undo=False):
        current_cell_center = Point(
                                (self.__top_left.x + self.__bottom_right.x)//2,
                                (self.__top_left.y+self.__bottom_right.y) //2
                                )
        to_cell_center = Point(
                                (to_cell.__top_left.x + to_cell.__bottom_right.x)//2,
                                (to_cell.__top_left.y+to_cell.__bottom_right.y) //2
                                )
        if not undo:
            color = "red"
        else:
            color = "gray"
        self.win.draw_line(
            Line(current_cell_center, to_cell_center),
            color
        )


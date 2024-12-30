from tkinter import Canvas
class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p0: Point, p1: Point):
        self.p0:Point = p0
        self.p1:Point = p1

    def draw(self, canvas: Canvas, fillColor: str):
        canvas.create_line(
            self.p0.x, self.p0.y, self.p1.x, self.p1.y,
            fill=fillColor,
            width=2,
        )


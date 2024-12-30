from cell import Cell
from window import Window
import time
from typing import Optional

import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Optional[Window]=None,
        seed: Optional[int]=None
    ):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells: list[list[Cell]] = []
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self.win))
            self._cells.append(col)
    
        self._break_entrance_and_exit()
        for colNum in range(len(self._cells)):
            for rowNum in range(len(self._cells[colNum])):
                self._draw_cell(colNum, rowNum)

        self._animate()
    
    def _draw_cell(self, colNum, rowNum):
        
        cell_top_left_x = colNum * self.cell_size_x + self.x1
        cell_top_left_y = rowNum * self.cell_size_y + self.y1

        cell_bottom_right_x = cell_top_left_x + self.cell_size_x
        cell_bottom_right_y = cell_top_left_y + self.cell_size_y

        cell: Cell = self._cells[colNum][rowNum]
        cell.draw(cell_top_left_x, cell_top_left_y, cell_bottom_right_x, cell_bottom_right_y)
    
    def _animate(self):
        while self.win:
            self._break_walls_r(0,0)
            self.win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        top_left_cell.has_top_wall = False

        bottom_right_cell = self._cells[-1][-1]
        bottom_right_cell.has_bottom_wall = False
        
    def _break_walls_r(self, colNum, rowNum):
        self._cells[colNum][rowNum].visited = True
        while True:
            toVisit = []
            canCheckLeft = colNum > 0
            canCheckRight = colNum < len(self._cells) - 1
            canCheckTop = rowNum > 0
            canCheckBottom = rowNum < len(self._cells[0]) - 1

            if canCheckLeft:
                if not self._cells[colNum-1][rowNum].visited:
                    toVisit.append((colNum-1, rowNum, "left"))

            if canCheckRight:
                if not self._cells[colNum+1][rowNum].visited:
                    toVisit.append((colNum+1, rowNum, "right"))
            
            if canCheckTop:
                if not self._cells[colNum][rowNum-1].visited:
                    toVisit.append((colNum, rowNum-1, "top"))

            if canCheckBottom:
                if not self._cells[colNum][rowNum+1].visited:
                    toVisit.append((colNum, rowNum+1, "bottom"))

            if len(toVisit) == 0:
                self._draw_cell(colNum, rowNum)
                return
            chosenDirPos = random.randrange(len(toVisit))
            nextCol, nextRow, dirToBreak = toVisit[chosenDirPos]

            currentCell:Cell = self._cells[colNum][rowNum]
            otherCell:Cell = self._cells[nextCol][nextRow]
            if dirToBreak == "left":
                currentCell.has_left_wall = False
                otherCell.has_right_wall = False
            
            if dirToBreak == "right":
                currentCell.has_right_wall = False
                otherCell.has_left_wall = False

            if dirToBreak == "top":
                currentCell.has_top_wall = False
                otherCell.has_bottom_wall = False

            if dirToBreak == "bottom":
                currentCell.has_bottom_wall = False
                otherCell.has_top_wall = False

            self._break_walls_r(nextCol, nextRow)

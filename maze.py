from units import Cell
from window import Window
import time
from typing import Optional
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
        if self.win:
            self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        top_left_cell.has_top_wall = False

        bottom_right_cell = self._cells[-1][-1]
        bottom_right_cell.has_bottom_wall = False
        
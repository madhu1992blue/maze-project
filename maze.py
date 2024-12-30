from units import Cell
from window import Window
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window,
    ):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(Cell(self.win))
            self._cells.append(row)
    
        for row in range(len(self._cells)):
            for col in range(len(self._cells[row])):
                self._draw_cell(row, col)

        self._animate()
    
    def _draw_cell(self, i, j):
        
        cell_top_left_x = j * self.cell_size_x + self.x1
        cell_top_left_y = i * self.cell_size_y + self.y1

        cell_bottom_right_x = cell_top_left_x + self.cell_size_x
        cell_bottom_right_y = cell_top_left_y + self.cell_size_y

        cell: Cell = self._cells[i][j]
        cell.draw(cell_top_left_x, cell_top_left_y, cell_bottom_right_x, cell_bottom_right_y)
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

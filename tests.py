import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_cell_start(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(5, 10, num_rows, num_cols, 10, 10)
        first_cell = m1.cells[0][0]
        
        self.assertEqual(
            first_cell.top_left.x,
            5
        )
        self.assertEqual(
            first_cell.top_left.y,
            10,
        )

    def test_maze_cell_end(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(5, 10, num_rows, num_cols, 10, 20)
        last_cell = m1.cells[-1][-1]
        
        self.assertEqual(
            last_cell.top_left.x,
            10 * (num_cols -1) + 5
        )
        self.assertEqual(
            last_cell.top_left.y,
            20 * (num_rows-1) + 10
        )
    
    def test_maze_cell_break(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(5, 10, num_rows, num_cols, 10, 20)
        last_cell = m1.cells[-1][-1]
        first_cell = m1.cells[0][0]
        self.assertEqual(
            last_cell.has_bottom_wall,
            False
        )
        self.assertEqual(
            first_cell.has_top_wall,
            False
        )
    
    def test_maze_cell_reset(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(5, 10, num_rows, num_cols, 10, 20)
        m1.cells[2][2].visited = True
        m1._reset_cells_visited()
        for col in m1.cells:
            for cell in col:
                self.assertEqual(cell.visited, False)
        

if __name__ == "__main__":
    unittest.main()
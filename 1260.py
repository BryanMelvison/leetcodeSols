from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # So for this problem, I used a simple approach to shift the grid. I calculated the new position of each element after shifting by k positions, and then placed it in the new position.
        # Easy way, no constraint:
        # Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid.
        # Space complexity: O(m*n) for the new grid.
        # Performance:
        # Runtime: faster than 83.13%
        # Memory Usage: beats 81.69%.
        row = len(grid)
        column = len(grid[0])
        grid_result = [[0] * column for idx in range(row)]

        for m in range(row):
            for n in range(column):
                row_add = (n + k) // column
                column_add = (n + k) % column
                grid_result[(m + row_add) % row][column_add] = grid[m][n]
        
        return grid_result

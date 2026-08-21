
from ast import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # This is a simple problem, we can just iterate through the list and keep track of the minimum path sum to reach the current cell by adding the minimum path sum to reach the cell above and the cell to the left.
        # Time complexity: O(m * n), where m is the number of rows and n
        # is the number of columns, we visit each cell once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 59.56%.
        # Memory Usage: less than 77.95%.
        row = len(grid)
        column = len(grid[0])
        for r in range(row):
            for c in range(column):
                if r - 1 >= 0 and c - 1 >= 0:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                elif r -1 >= 0:
                    grid[r][c] += grid[r-1][c]
                elif c - 1 >= 0:
                    grid[r][c] += grid[r][c-1]
        return grid[-1][-1]

        
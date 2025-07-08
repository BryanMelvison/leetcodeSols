from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # We can just keep track of the rows and columns in a dict, then we can just multiply the counts
        # Time complexity, O(n^2) : We need to iterate through the grid to get the rows and columns
        # Space complexity, O(n^2) : We need to store the rows and columns in a dict
        # Performance:
        # Runtime: faster than 78.14%
        # Memory Usage: less than 60.08%.
        # Put in set
        store_row = {}
        store_col = {}

        for r_num in range(len(grid)): 
            # For row:
            row_key = tuple(grid[r_num])
            store_row[row_key] = store_row.get(row_key, 0) + 1 

            # For column:
            col = [grid[idx][r_num] for idx in range(len(grid))]
            col_key = tuple(col)
            store_col[col_key] = store_col.get(col_key, 0) + 1

        # Count total:
        total = 0
        for key,value in store_row.items():
            if key in store_col:
                total += value * store_col[key]
        return total
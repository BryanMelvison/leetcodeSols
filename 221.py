# typing 
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Why do we need to check just adjacent cells? Because we are looking for a square, so if the adjacent cells are not 1, then we cannot form a square. We can use dynamic programming to keep track of the maximum size of the square that can be formed at each cell. The maximum size of the square that can be formed at a cell is equal to the minimum of the maximum sizes of the squares that can be formed at the adjacent cells plus 1.
        # Time complexity: O(m * n), where m is the number of rows and n
        # is the number of columns, we visit each cell once.
        # Space complexity: O(m * n), we are using a list to store the maximum size of the square that can be formed at each cell.
        # Performance:
        # Runtime: faster than 72.31%.
        # Memory Usage: less than 48.79%.

        int_matrix = []
        for mat in matrix:
            row = []
            for m in mat:
                row.append(1 if m == "1" else 0)
            int_matrix.append(row)
        maximum = 0
        for r in range(0, len(int_matrix)):
            for c in range(0, len(int_matrix[0])):
                if int_matrix[r][c] != 1:
                    continue
                if r - 1 >= 0 and c - 1 >= 0:
                    current = 1 + min(int_matrix[r-1][c], int_matrix[r][c-1], int_matrix[r-1][c-1] )
                    if current > maximum:
                        maximum = current
                    int_matrix[r][c] = current
                else:
                    if int_matrix[r][c] > maximum:
                        maximum = int_matrix[r][c]
        return maximum * maximum

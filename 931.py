from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # This is a simple problem, we can just iterate through the list and keep track of the minimum path sum to reach the current cell by adding the minimum path sum to reach the cell above and the cell to the left.
        # Time complexity: O(n^2), where n is the number of rows in the
        # matrix, we visit each cell once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 55.01%.
        # Memory Usage: less than 60.37%.
        for r in range(1, len(matrix)):
            for c in range(len(matrix[r])):
                if c == 0:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])
                elif c == len(matrix[r]) - 1:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1])
                else:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1], matrix[r-1][c+1])
        return min(matrix[-1])

                    
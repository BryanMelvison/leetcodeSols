class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # This is a simple problem, we can just iterate through the list and keep track of the number of ways to reach the current cell by adding the number of ways to reach the cell above and the cell to the left.
        # Time complexity: O(m * n), where m is the number of rows and n
        # is the number of columns, we visit each cell once.
        # Space complexity: O(m * n), we are using a list to store the number
        # of ways to reach each cell.
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 42.65%.
        current_paths = [[0] * n for _ in range(m)]
        current_paths[0][0] = 1
        for row in range(m):
            for column in range(n): 
                if row-1 >= 0:
                    current_paths[row][column] += current_paths[row-1][column]
                if column - 1 >= 0:
                    current_paths[row][column] += current_paths[row][column-1]
        return current_paths[-1][-1]
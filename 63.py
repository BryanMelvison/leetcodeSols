
from ast import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DPDPDP, with extra condition, blocking 0 if obstacle
        # Time complexity: O(m * n), where m is the number of rows and n
        # is the number of columns, we visit each cell once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 61.27%.
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        obstacleGrid[0][0] = -1 if obstacleGrid[0][0] != 1 else 0
        for r in range(row):
            for c in range(col):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                    continue
                if r - 1 >= 0 and c - 1 >= 0:
                    obstacleGrid[r][c] += obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
                elif r - 1 >= 0:
                    obstacleGrid[r][c] += obstacleGrid[r - 1][c]
                elif c - 1 >= 0:
                    obstacleGrid[r][c] += obstacleGrid[r][c - 1]
        return -1 * obstacleGrid[-1][-1]

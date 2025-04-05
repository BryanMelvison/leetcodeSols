from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Go through each row, x and y:
        # Try iterating, swapping it
        # 0 1 2
        # 2 1 0 
        # 00 = 00
        # 01 = 10
        # 02 = 20
        # -> 
        # 1 4 7
        # 2 5 6
        # 3 8 9
        # 1 4 7 is the reverse of 7 4 1
        # hmmm, so after transposing the first iter, I think we just reverse
        # Next iteration, 1,1 1,2, we limit the inner iter scope

        # Time complexity, O(n^2) : double for loop
        # Space complexity, O(1) : Constant

        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 67.35%.

        for x in range(len(matrix)):
            for y in range(x, len(matrix)):
                # Buffer
                temp = matrix[x][y] 
                matrix[x][y] = matrix[y][x]
                matrix[y][x] = temp

        # Reverse, in place operation:
        for row in range(len(matrix)):
            matrix[row].reverse()


from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # This is a simple problem, we can just iterate through the list and keep track of the minimum path sum to reach the current cell by adding the minimum path sum to reach the cell above and the cell to the left.
        # Time complexity: O(n^2), where n is the number of rows in the triangle, we visit each cell once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 76.44%.
        # Memory Usage: less than 63.33%.

        for idx in range(1, len(triangle)):
            for index in range(len(triangle[idx])):
                if index -1 >= 0 and index < len(triangle[idx]) - 1:
                    triangle[idx][index] += min(triangle[idx-1][index-1], triangle[idx-1][index])
                elif index < len(triangle[idx]) - 1:
                    triangle[idx][index] += triangle[idx-1][index]
                else:
                    triangle[idx][index] += triangle[idx-1][index-1]
        
        return min(triangle[-1])
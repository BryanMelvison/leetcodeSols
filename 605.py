from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # We can just iterate through the flowerbed, and check if we can place a flower at each position
        # We can place a flower if the current position is empty (0), and both the left and right positions are also empty (0)
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : No extra space used
        # Performance:
        # Runtime: faster than 74.25%.
        # Memory Usage: less than 35.22%.
        countPlace = 0
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 0:
                canPlantLeft = (i == 0) or (flowerbed[i - 1] == 0) # We don't care about LHS for the first edge (negative indexing for python)
                canPlantRight = (i == size - 1) or (flowerbed[i + 1] == 0) # We don't care about RHS if error for last edge, since it is already True for the LHS
                # If placeable:
                if canPlantLeft and canPlantRight:
                    flowerbed[i] = 1
                    countPlace += 1

                    if countPlace >= n:
                        return True

        return countPlace >= n
            
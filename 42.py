from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # left side:
        # Intuitive, left and right sweep, then find the minimum of each sweep, total them up
        # Time complexity, O(n) :  multiple for loops
        # Space complexity, O(n) : array containing the excess water for each sweep (x2)

        # Performance:
        # Runtime: faster than 54.98%.
        # Memory Usage: less than 5.88%.

        current_max = height[0]
        left_side = []
        for side in height:
            if side > current_max:
                current_max = side
            left_side.append(current_max - side)

        current_max = height[-1]
        right_side = []
        for side in height[::-1]:
            if side > current_max:
                current_max = side
            right_side.append(current_max - side)

        final = 0
        for left,right in zip(left_side, right_side[::-1]):
            final += min(left ,right)
        
        return final
        
        
        # right side:
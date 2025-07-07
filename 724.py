from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # We iterate through the array and keep track of the sum of the left and right side of the current index.
        # If the left and right side are equal, we return the index.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : We are not using any extra space
        # Performance:
        # Runtime: faster than 91.92%.
        # Memory Usage: less than 38.67%.
        total = sum(nums)
        left = 0
        right = total
        for idx, num in enumerate(nums):
            if idx != 0:
                left += nums[idx - 1]
            right -= num
            if left == right:
                return idx
        return -1
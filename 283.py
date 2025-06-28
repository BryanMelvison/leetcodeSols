from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We use two pointers, one for the left and one for the right.
        # The left pointer will slide through the array on every swap,
        # and the right pointer will iterate through the array, finding non-zero elements.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : We are not using any extra space
        # Performance:
        # Runtime: faster than 84.05%. 
        # Memory Usage: less than 49.19%.
        left = 0 # left is zero
        for right in range(len(nums)):
            if nums[right] != 0: # right is num
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
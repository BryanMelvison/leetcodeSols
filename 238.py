from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This is a simple problem, we just need to keep track of the product of all elements to the left and right of the current element.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : We need to store the product of all elements in an array
        # Performance:
        # Runtime: faster than 67.1%.
        # Memory Usage: less than 54.19%.
        len_arr = len(nums)
        arr = [1] * len_arr
        temp_value = 1
        for idx in range(1, len_arr):
            temp_value *= nums[idx - 1]
            arr[idx] *= temp_value

        temp_value = 1
        for idx in range(len_arr - 2, -1, -1):
            temp_value *= nums[idx + 1]
            arr[idx] *= temp_value

        return arr
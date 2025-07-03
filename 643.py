from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # We can use a sliding window approach to find the maximum average of k consecutive elements.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : We are not using any extra space
        # Performance:
        # Runtime: faster than 96.47%
        # Memory Usage: less than 77.47%.
        current_nums = sum(nums[:k])
        max_nums = current_nums
        for idx in range(k, len(nums)):
            current_nums +=  nums[idx] - nums[idx - k] 
            if max_nums < current_nums:
                max_nums = current_nums
        
        return max_nums / k

        
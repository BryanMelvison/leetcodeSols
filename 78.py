from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # So I used recursion to get all the subsets, for each number, we can either include it or not include it, so we can do this recursively, and keep track of the current subset and the remaining numbers to explore.
        # Time complexity, O(2^n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the current subset
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 66.92%.
        result = []
        
        def recursion(current, nums):
            result.append(current)
            if len(nums) >= 1:
                for idx, num in enumerate(nums):
                    current.append(num)
                    recursion(current.copy(), nums[idx + 1:])
                    current.pop(-1)
                
        recursion([], nums)
        return result
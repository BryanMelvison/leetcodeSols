from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Just keep track of the num not explored, if not explored pass in the diff between the numbers
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the dict

        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 6.32%.

        explored = {}
        for idx, num in enumerate(nums):
            if num not in explored:
                diff = target - num
                explored[diff] = idx
            else:
                return [explored[num], idx]
        return []
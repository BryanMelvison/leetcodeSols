from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # Use recursion, we need to go through all subset
        # Remember this:
        # For XOR Bit manipulation: to get the individual value of each element, 0 ^ num = num.
        # Also for computing the XOR of the subset, I keep track of the value recursively to go through every possible combination of subset
        # Time complexity, O(2^n)
        # Space complexity, O(n) (n recursive stack) (o(n) auxiliary space)

        # Performance:
        # Runtime: faster than 55.46%.
        # Memory Usage: less than 96.02%.

        total = 0
        def countXORSum(curr_value, curr_idx):
            nonlocal total
            if curr_idx == len(nums):
                return
            for idx, num in enumerate(nums[curr_idx:]):
                total += curr_value^num
                countXORSum(curr_value ^ num, curr_idx + 1 + idx)
        
        countXORSum(0, 0)
        return total














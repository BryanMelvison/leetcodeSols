from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # This problem is about finding a 132 pattern in a given list of integers. The approach I used is to iterate through the list from the end to the beginning, keeping track of the third element of the pattern (the "2" in "132") and using a stack to keep track of potential candidates for the first element (the "1" in "132"). If we find a number that is less than the third element, we have found a 132 pattern.
        # Time complexity: O(n) where n is the number of elements in the list.
        # Space complexity: O(n) for the stack.
        # Performance:
        # Runtime: faster than 58.72%
        # Memory Usage: beats 69.28%.
        stack = []
        third = float("-inf")
        for idx in range(len(nums) - 1, -1,-1 ):
            if nums[idx] < third:
                return True
            while stack and stack[-1] < nums[idx]:
                third = stack.pop()
            stack.append(nums[idx])

        return False
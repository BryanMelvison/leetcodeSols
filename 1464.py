from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # This problem is about finding the maximum product of two digits in a given list of integers. The approach I used is to iterate through the list, keeping track of the two largest numbers found so far. At the end of the iteration, I return the product of these two numbers minus one.
        # Time complexity: O(n) where n is the number of elements in the list.
        # Space complexity: O(1) since we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 68.04%
        max_one = 0
        max_second = 0
        for num in nums:
            if num >= max_one:
                if max_one > max_second:
                    max_second = max_one
                max_one = num
            elif num > max_second:
                max_second = num
        return (max_one - 1) * (max_second -1)
        
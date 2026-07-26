from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # This problem is about finding the maximum product of three numbers in a given list of integers. The approach I used is to iterate through the list, keeping track of the three largest and two smallest numbers found so far. At the end of the iteration, I return the maximum product of either the three largest numbers or the two smallest numbers multiplied by the largest number.
        # Time complexity: O(n) where n is the number of elements in the list.
        # Space complexity: O(1) since we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 42.28%.
        first = -1001
        second = -1001
        third = -1001
        first_min = 1001
        second_min = 1001
        for num in nums:
            if num >= first:
                if first >= second:
                    if second >= third:
                        third= second
                    second = first
                first = num
            elif num >= second:
                if second >= third:
                    third = second
                second = num
            elif num >= third:
                third = num
            
            if first_min >= num:
                if first_min <= second_min:
                    second_min = first_min
                first_min = num
            elif second_min >= num:
                second_min = num
        return max(first * second * third, first_min * second_min * first)

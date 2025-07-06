from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # I use a sliding window approach to find the longest subarray with at most k zeros.
        # Time complexity, O(n) : We iterate through the list once
        # Space complexity, O(1) : We use a few variables to keep track of the pointers and the count of zeros
        # Performance:
        # Runtime: faster than 78.79%
        # Memory Usage: less than 80.63%.
        # Ill try to do it with sliding window:
        first_ptr = 0
        zero_track = 0
        max_leng = 0
        for second_ptr in range(len(nums)):
            if nums[second_ptr] == 0:
                zero_track += 1

            # Now move the left pointer:
            while zero_track > k:
                if nums[first_ptr] == 0:
                    zero_track -= 1
                first_ptr += 1

            # Update max length:
            max_leng = max(max_leng, second_ptr - first_ptr + 1)

        return max_leng
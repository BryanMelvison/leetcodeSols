
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # This is a simple problem, we can just iterate through the list and keep track of the minimum and maximum index of the numbers, then we can calculate the minimum number of deletions needed to remove both the minimum and maximum numbers from the list.
        # Time complexity: O(n), where n is the length of the nums list, we
        # visit each element once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 73.11%.
        # Memory Usage: less than 80.37%.
        min_idx, max_idx = 0,0
        total_len = len(nums)
        for idx in range(total_len):
            if nums[idx] > nums[max_idx]:
                max_idx = idx
            if nums[idx] < nums[min_idx]:
                min_idx = idx
        
        first = min(min_idx, max_idx)
        last = max(min_idx, max_idx)
        return min(total_len-first, last + 1, total_len - (last - first - 1))

        
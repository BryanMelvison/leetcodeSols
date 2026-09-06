from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # For this, we can use a greedy approach, we can keep track of the maximum index we can reach, and if at any point the maximum index we can reach is less than the current index, we return False, otherwise we return True.
        # Time complexity: O(n), where n is the length of the nums list, we
        # visit each element once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 91.46%.
        # Memory Usage: less than 84.89%.
        dest = len(nums) - 1
        local_dest = nums[left]

        for left, val in enumerate(nums):
            if local_dest < left:
                return False
            if local_dest >= dest:
                return True
            local_dest = max(local_dest, left +val)
        return False
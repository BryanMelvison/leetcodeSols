from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # This is a binary search problem, we can use binary search to find the minimum maximum distance between pairs.
        # Here, we are trying to find the maximum distance between pairs such that we can form at least p pairs.
        # We can sort the array and then use binary search to find the minimum maximum distance.
        # We will use a helper function to check if we can form at least p pairs with the given maximum distance.
        # Time complexity, O(n log m) : n is the length of nums, m is the maximum distance between pairs
        # Space complexity, O(1) : We are not using any extra space
        # Performance:
        # Runtime: faster than 65.98%.
        # Memory Usage: less than 98.91%.
        nums.sort()
        len_nums = len(nums)
         
        # Try using Binary Search Tree
        left = 0
        right = nums[-1] - nums[0]
        res = float('-inf')

        def isValid(mid):
            count, i = 0, 0
            while i < len_nums -1:
                if nums[i + 1] - nums[i] <= mid:
                    i += 2
                    count += 1
                else:
                    i += 1
            return count >= p

        while left <= right:
            print(left, right)

            mid = (left + right) // 2
            if isValid(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
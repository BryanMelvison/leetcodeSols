class Solution:
    def jump(self, nums: List[int]) -> int:
        # For this, we can use a dynamic programming approach, we can keep track of the minimum number of jumps needed to reach each index, and return the value at the last index.
        # Time complexity: O(n^2), where n is the length of the nums list, we visit each element once and for each element we check all previous elements.
        # Space complexity: O(n), we are using a list to store the minimum number of jumps needed to reach each index.
        # Performance:
        # Runtime: faster than 19.78%.
        # Memory Usage: less than 65.94%.
        result = [0] * (len(nums))
        nums = nums[::-1]
        for idx, num in enumerate(nums[1:], start = 1):
            if num == 0:
                result[idx] = float('inf')
                continue
            # Calculate end and start
            end = max(0, idx - num) 
            curr = idx 
            result[idx] = min(result[end: curr]) + 1
        print(result)
        return result[-1]
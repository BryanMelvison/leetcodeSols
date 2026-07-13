from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Since need to do it twice, can run it twice here :p nums + nums
        # We scrap this solution, dumb me, I think can do it in a more efficient manner, 
        # so instead we do this, for the circular, we can still do it in 1 loop, but for the "circle", we identiy which is the max index
        # so loop is from the index after max_index to max_index, so we do it in 1 go O(n)
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the stack
        # Performance:
        # Runtime: faster than 95.46%
        # Memory Usage: beats 58.11%
        max_idx = nums.index(max(nums))
        # how to turn 1 to -1... -1 to 1
        total = len(nums)
        result = [-1] * total
        stack = []
        for idx in range(max_idx - total + 1, max_idx + 1, 1):
            while len(stack) != 0 and nums[idx] > nums[stack[-1]]:
                current_idx = stack.pop(-1)
                result[current_idx] = nums[idx]
            stack.append(idx)
        return result

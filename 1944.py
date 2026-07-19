from typing import List
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # So for this problem, I used a stack to keep track of the heights and the total number of people that can be seen by the current person. For each height, we pop from the stack until we find a height that is greater than the current height, and we add the total number of people that we popped to the total number of people for the current height.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the stack
        # Performance:
        # Runtime: faster than 49.26%
        # Memory Usage: beats 27.09%.
        total = len(heights)
        result = [0] * total
        stack = []
        for idx in range(total):
            h = heights[idx]
            while stack and heights[stack[-1]] < h:
                result[stack.pop(-1)] += 1

            if stack:
                result[stack[-1]] += 1
  
            stack.append(idx)
        return result


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # So I used monolithic decreasing stack to keep track of temperatures where they have not seen any higher temperatures yet, once higher temperature is seen, we pop it from the stack to get the index, and calculate the difference between the current index and the popped index to get the number of days until a warmer temperature.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the stack
        # Performance:
        # Runtime: faster than 37.89%
        # Memory Usage: beats 55.84%.
        current = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop(-1)
                current[idx] = i - idx
            stack.append(i)
        
        return current
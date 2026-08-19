class Solution:
    def climbStairs(self, n: int) -> int:
        # This is a simple problem, we can just iterate through the list and keep track of the number of ways to reach the current stair by adding the number of ways to reach the previous two stairs.
        # Notice pattern is fibonacci sequence, we can use two variables to keep track of the previous two stairs and update them as we iterate through the list.
        # Time complexity: O(n), where n is the number of stairs, we visit each stair once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 95.88%.
        first = 1
        second = 2
        if n == 1:
            return first
        if n == 2: 
            return second
        
        for n in range(3, n + 1):
            first, second = second, first + second
        
        return second
        
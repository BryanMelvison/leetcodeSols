class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Same as power of 2 with a twist, additional check for 3:
        # Time complexity: O(1)
        # Space complexity: O(1)
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 61.52%
        if n ==0: return False
        return (n & n-1 == 0) and (n-1) % 3 ==0
        
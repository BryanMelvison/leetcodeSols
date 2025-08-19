class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Since 3 is also prime, can utilize the fact that the: highest prime number contained within int is only divisible by powers of 3:
        # 3**19 = 1162261467, which is the highest power of 3 that fits within a 32-bit signed integer.
        # Time complexity: O(1)
        # Space complexity: O(1)
        # Performance: 
        # Runtime: faster than 100%
        # Memory Usage: less than 72.16%
        maxi = 3**19 # anything higher is above contraint
        if n <= 0: return False
        return maxi % n == 0
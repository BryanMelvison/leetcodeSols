class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Normal way: What I would have done:
        # iteratively / recursively:
        # Time complexity: O(log n)
        # Space complexity: O(1)
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 55.53%
        # while n > 1:
        #     n /= 2
        # return n == 1
        
        # Genius way:
        # since multiple of 2s are represented as these in binary:
        # 1: 1, 2: 10, 4: 100, 8: 1000
        # See the pattern? so now we just have to perform bitwise AND operation with the number before them, and if we get 0, its power of 2:
        # 7 & 8 = 0: 0111 & 1000 = 0
        # Time complexity: O(1)
        # Space complexity: O(1)
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 55.53%
        if n == 0:
            return False
        return  True if n & (n-1) == 0 else False
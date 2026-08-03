class Solution:
    def tribonacci(self, n: int) -> int:
        # This problem is about finding the n-th number in the Tribonacci sequence, which is defined as T(n) = T(n-1) + T(n-2) + T(n-3) with base cases T(0) = 0, T(1) = 1, and T(2) = 1. The approach I used is to use dynamic programming to store the previously computed values in a dictionary, and then recursively compute the n-th value using these stored values.
        # Time complexity: O(n) where n is the input number.
        # Space complexity: O(n) for the dictionary storing the computed values.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 54.97%.
        collection = {0: 0, 1: 1, 2: 1}

        def dp(n):
            if n not in collection:
                collection[n] = dp(n-1) + dp(n-2) + dp(n-3)
            return collection[n]

        return dp(n)
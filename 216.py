from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # So I used recursion to get all the combinations, for each number, we can either include it or not include it, so we can do this recursively, and keep track of the current combination and the remaining numbers to explore.
        # Time complexity, O(2^n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the current combination
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 93.45%.
        # n:target, k:total
        used = 0
        result = []

        def combination(current, used, target, idx):
            if used == k:
                if target == 0:
                    result.append(current)
                return
            if target <= 0:
                return
            for num in range(idx, 10):
                current.append(num)
                combination(current[:], used + 1, target - num, num + 1)
                current.pop(-1)
        combination([], 0, n, 1)
        return result
                
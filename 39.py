from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # So I used recursion to get all the combinations, for each number, we can either include it or not include it, so we can do this recursively, and keep track of the current combination and the remaining numbers to explore.
        # Time complexity, O(2^n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the current combination
        # Performance:
        # Runtime: faster than 48.80%
        # Memory Usage: beats 32.06%.
        result = []

        def find_combine(target, current, candidates):
            if target == 0:
                result.append(current)
            if target > 0:
                for idx, candidate in enumerate(candidates):
                    current.append(candidate)
                    find_combine(target - candidate, current[:], candidates[idx:])
                    current.pop(-1)
        find_combine(target, [], candidates)
        return result

                
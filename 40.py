from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # So I used recursion to get all the combinations, for each number, we can either include it or not include it, so we can do this recursively, and keep track of the current combination and the remaining numbers to explore.
        # Time complexity, O(2^n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the current combination
        # Performance:
        # Runtime: faster than 44.64%
        # Memory Usage: beats 89.80%.

        candidates.sort()
        result = []
        def combine_sum(previous, target, current, candidates):
            if target == 0:
                result.append(current)
                return
            if target > 0:
                for idx, candidate in enumerate(candidates):
                    if candidate == previous:
                        continue
                    current.append(candidate)
                    combine_sum(-1, target - candidate, current[:], candidates[idx + 1:])
                    current.pop(-1)
                    previous = candidate

        combine_sum(-1, target, [], candidates)
        return result
        
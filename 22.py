from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # So I used recursion to get all the combinations, for each number, we can either include it or not include it, so we can do this recursively, and keep track of the current combination and the remaining numbers to explore.
        # Time complexity, O(2^n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the current combination
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 72.74%.

        result = []

        def generate(left, right, current):
            if left == right and left == n:
                result.append(current)
                return
            if left < n:
                generate(left + 1, right, current + "(")
            if right < left: 
                generate(left, right + 1, current + ")")

        generate(0,0, "")
        return result
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # So I used recursion to get all the combinations, for each number, we can either include it or not include it, so we can do this recursively, and keep track of the current combination and the remaining numbers to explore.
        # Time complexity, O(2^n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the current combination
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 95.53%.
        result = []
        length = len(digits)
        mapping = {"2": "abc", "3":"def", "4": "ghi", "5":"jkl", "6": "mno", "7":"pqrs", "8": "tuv", "9":"wxyz"}
        def combination(current, idx):
            if idx + 1 > length:
                result.append(current)
                return
            for digit in mapping[digits[idx]]:
                current += digit
                combination(current, idx + 1)
                current = current[:-1]
        combination("", 0)
        return result
            
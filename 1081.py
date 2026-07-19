class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # So for this problem, I used a greedy approach to get the smallest subsequence, for each character, we can either include it or not include it, so we can do this iteratively, and keep track of the current subsequence and the remaining characters to explore.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the current subsequence
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 95.34%.
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        seen = set()
        result = []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            
            while result and result[-1] > char and counter[result[-1]] > 0:
                seen.remove(result.pop(-1))
            
            seen.add(char)
            result.append(char)
        return "".join(result)

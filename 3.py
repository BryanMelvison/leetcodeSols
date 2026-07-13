class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Just keep track of the num not explored, if not explored pass in the diff between the numbers
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the dict
        # Performance:
        # Runtime: faster than 87.98%
        # Memory Usage: beats 68.21%.
        max_len = 0
        left = 0
        window_char = set()
        for right in range(len(s)):
            if s[right] not in window_char:
                window_char.add(s[right])
            else:
                while s[right] in window_char:
                    window_char.remove(s[left])
                    left += 1
                window_char.add(s[right])

            if max_len <= right - left:
                max_len = right-left + 1

        return max_len
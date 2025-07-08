class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # The rules and test cases imply that the length must be the same, must use existing character, should maintain consistent total frequency per character
        # Time complexity, O(n) : We iterate through the string once
        # Space complexity, O(n) : We use a Counter to count the frequency of characters
        # and a set to check if the characters are the same.
        # We also use a Counter to count the frequency of frequencies.
        # This is a more efficient way to check if the two strings are close.
        # Performance:
        # Runtime: faster than 90.52%
        # Memory Usage: less than 19.55%.
        from collections import Counter
        if len(word1) == len(word2):
            if set(word1) == set(word2):
                return Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        return False
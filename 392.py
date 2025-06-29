class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # We can use two pointers, one for each string.
        # We will iterate through the second string and check if the characters in the first string are present in order.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : We are not using any extra space
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 24.08%.
        if s == "":
            return True

        pointer = 0

        for char in t:
            if s[pointer] == char:
                pointer += 1
            if pointer == len(s):
                return True
        return pointer == len(s) 
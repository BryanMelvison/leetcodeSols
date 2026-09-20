class Solution:
    def reverseDegree(self, s: str) -> int:
        # For this, we can just iterate through the string and for each character, we can calculate the degree by taking the difference between the character and 'a' and adding 1. Then we can multiply that by the index + 1 to get the degree for that character. Finally, we can sum all the degrees to get the total degree.
        # Time complexity: O(n), where n is the length of the string, we visit each character once.
        # Space complexity: O(1), we are using a constant amount of space to store the total degree.
        # Performance:
        # Runtime: faster than 70.00%.
        # Memory Usage: less than 19.13%.
        total = 0
        for idx in range(len(s)):
            total += (26 - (ord(s[idx]) - 97)) * (idx + 1)
        return total
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # My first approach was to iterate through the string and check for three consecutive digits.
        # However, I realized that we can optimize this by checking for the largest digit first.
        # We can iterate from 9 to 0 and check if the digit appears three times in a row.
        # This way, we can immediately return the largest good integer found.
        # Time complexity: O(n), where n is the length of the string.
        # Space complexity: O(1) since we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 58.98%.
        for n in range(9, -1, -1):
            string = str(n) * 3
            if string in num:
                return string
        return ""
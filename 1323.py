class Solution:
    def maximum69Number (self, num: int) -> int:
        # This is a simple problem, we just need to find the first occurrence of 6 in the number and change it to 9.
        # We can convert the number to a string, find the first occurrence of 6,
        # change it to 9, and then convert it back to an integer.
        # Time complexity: O(n), where n is the number of digits in the number.
        # Space complexity: O(n), since we are converting the number to a string.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 77.29%.
        digits = list(str(num))
        for i in range(len(digits)):
            if digits[i] == "6":
                digits[i] = "9"
                break
        return int("".join(digits))

        
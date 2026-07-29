class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # I just realized... this is assuming string is palindromic, I thought it's not a palindromic string lol
        # This problem is about finding the smallest palindromic string that can be formed by rearranging the characters of a given string. The approach I used is to count the occurrences of each character in the string, and then construct the first half of the palindrome by taking half of the occurrences of each character. If there is an odd occurrence of any character, I place it in the middle of the palindrome. Finally, I construct the second half of the palindrome by reversing the first half and concatenating it with the middle character (if any).
        # Time complexity: O(n) where n is the number of characters in the string.
        # Space complexity: O(1) since we are using a constant amount of space for the character count.
        # Performance:
        # Runtime: faster than 38.39%
        # Memory Usage: beats 51.79%.
        counter =  {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        first = ""
        middle = ""
        last = ""

        for char in "abcdefghijklmnopqrstuvwxyz":
            if char not in counter:
                continue
            val = counter[char]
            while val > 0:
                if val == 1:
                    middle += char
                    val -= 1
                elif val > 1:
                    remainder = val % 2
                    division = val // 2
                    val = division + remainder
                    first += division * char
                    last = division * char + last
                    val -= division
        if first != "":
            return first + middle + last
        return middle
                
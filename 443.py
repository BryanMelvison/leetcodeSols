from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        # This ia an O(1) space complexity solution to the problem.
        # We use two pointers to keep track of the current character and the next character.
        # If the next character is different, we add the current character and its count to the result.
        write = 0
        anchor = 0
        for read in range(len(chars) + 1):
            if read == len(chars) or chars[anchor] != chars[read]:
                chars[write] = chars[anchor]
                write += 1
                if read - anchor > 1:
                    for char in str(read-anchor):
                        chars[write] = char
                        write += 1
                anchor = read
        return write
        # Below is an O(n) time complexity solution to the problem.
        # We just need to keep track of the current character and how many times it has appeared.
        # If the next character is different, we add the current character and its count to the result.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : We are using a string to store the result, which can be at most n characters long.
        # Performance:
        # Runtime: faster than 100%
        # # Memory Usage: less than 94.17%.
        if len(chars) == 1:
            return 1
        current = chars[0]
        track = 1
        result = ""
        for idx in range(1, len(chars)):
            if chars[idx] != current:
                # add to result:
                result += current 
                if track != 1:
                    result += str(track)
                current = chars[idx]
                track = 1
            else: 
                track += 1
        result += current
        if track != 1:
            result += str(track)
        for idx, c in enumerate(result):
            chars[idx] = c

        return len(result)
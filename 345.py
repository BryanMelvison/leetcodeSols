class Solution:
    def reverseVowels(self, s: str) -> str:
        # Two pointer approach, one from the left and one from the right, swap when both are vowels
        # Since strings are immutable, we will convert to a list first
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the list
        # Performance:
        # Runtime: faster than 90.28%.
        # Memory Usage: less than 68.68%.

        vowels = {"a", "A", "I", "i", "u", "U", "e", "E", "o", "O"}
        len_word = len(s)
        left_pointer = 0
        right_pointer = len_word - 1
        s = list(s)
        while left_pointer < right_pointer:
            # Look for vowels on the left side:
            while s[left_pointer] not in vowels:
                left_pointer += 1
                if left_pointer >= len_word:
                    break
            while s[right_pointer] not in vowels:
                right_pointer -= 1
                if right_pointer < 0:
                    break

            if left_pointer < right_pointer:
                # must be vowels:
                left = s[left_pointer]
                right = s[right_pointer]
                s[left_pointer], s[right_pointer] = right, left
        
            left_pointer += 1
            right_pointer -= 1
            
        return "".join(s)
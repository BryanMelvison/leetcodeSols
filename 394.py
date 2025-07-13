class Solution:
    def decodeString(self, s: str) -> str:
        # We can use a stack to keep track of the characters and numbers.
        # When we encounter a number, we push it onto the stack.
        # When we encounter a "[", we push the current number onto the stack.
        # When we encounter a "]", we pop the last number from the stack and repeat the string that many times.
        # Time complexity, O(n * k) : We iterate through the string once, and in the worst case, we repeat a string k times. Where k is the maximum number of repetitions.
        # Space complexity, O(n) : In the worst case, we store all characters in the stack
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 97.14%.
        # Since we assume it's a valid string:
        stack = []
        number = ""
        word = ""
        for char in s:
            # Find number:
            if char.isnumeric():
                if word != "":
                    stack.append(word)
                    word = ""
                number += char
            elif char == "[":
                stack.append(number)
                number = ""
            elif char == "]":
                print(stack)
                # Recursively check for integer:
                temp_word = word
                while stack:
                    print(temp_word)
                    curr_pop = stack.pop()
                    if curr_pop.isnumeric():
                        temp_word = int(curr_pop) * temp_word
                        stack.append(temp_word)
                        break
                    else:
                        temp_word = curr_pop + temp_word
                word = ""
            else:
                word += char

        if word != "":
            stack.append(word)

        return "".join(stack)
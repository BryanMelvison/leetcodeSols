class Solution:
    def removeStars(self, s: str) -> str:
        # We can use a stack to keep track of the characters.
        # When we encounter a star, we pop the last character from the stack.
        # Time complexity, O(n) : We iterate through the string once
        # Space complexity, O(n) : In the worst case, we store all characters in the stack
        # Performance:
        # Runtime: faster than 66.55%
        # Memory Usage: less than 58.56%.
        
        stack = []
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)
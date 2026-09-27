class Solution:
    def reverseParentheses(self, s: str) -> str:
        # For ( bracket sign: whatever is inside, append, 
            # If found another bracket sign, current bit is appended first
        # if ) is found, pop the stack, and append the reversed bit, and append back
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the stack
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 29.73%.
        current = ""
        stack = []
        for c in s: 
            if c == "(":
                stack.append(current)
                current = ""
            elif c == ")":
                current = current[::-1]
                temp = stack.pop()
                current = temp + current
            else:
                current += c
        return current
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # For this, we can use a stack to keep track of the numbers we have seen so far, and when we see an operator we pop the last two numbers from the stack, perform the operation and push the result back onto the stack. At the end, we return the last number in the stack.
        # Time complexity: O(n), where n is the length of the tokens list, we
        # visit each element once.
        # Space complexity: O(n), we are using a stack to store the numbers we have
        # seen so far.
        # Performance:
        # Runtime: faster than 54.75%.
        # Memory Usage: less than 36.08%.
        stack = []
        for token in tokens:
            if token in "+/-*":
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    stack.append(int(first) + int(second))
                elif token == "*":
                    stack.append(int(first) * int(second))
                elif token == "-":
                    stack.append(int(second) - int(first))
                elif token == "/":
                    stack.append(int(second/first))
            else:
                stack.append(int(token))
        return stack[-1]
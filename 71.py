class Solution:
    def simplifyPath(self, path: str) -> str:
        # For this, we can use a stack to keep track of the directories we have seen so far, and when we see a ".." we pop the last directory from the stack, and when we see a "." we do nothing. At the end, we join the stack with "/" and return it.
        # Time complexity: O(n), where n is the length of the path string, we visit each character once.
        # Space complexity: O(n), we are using a stack to store the directories we have
        # seen so far.
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 25.63%.
        path_str = path.split("/")
        stack = []
        for item in path_str:
            if item == "":
                continue
            elif item == "..":
                if stack:
                    stack.pop(-1)
            elif item == ".":
                continue
            else:
                stack.append(item)
        return "/" + "/".join(stack)
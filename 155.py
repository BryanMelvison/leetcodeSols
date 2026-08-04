class MinStack:
    # Time complexity: O(1) for all operations (push, pop, top, getMin)
    # Space complexity: O(n) where n is the number of elements in the stack,
    # since we are storing the elements in two separate stacks (one for the values and one
    # for the minimum values).
    # Performance:
    # Runtime: faster than 81.34%
    # Memory Usage: beats 73.00%.
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:
        if not self.min or value < self.min[-1]:
            self.min.append(value)
        else: 
            self.min.append(self.min[-1])
        self.stack.append(value)
        
    def pop(self) -> None:
        self.stack.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
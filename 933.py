class RecentCounter:
    def __init__(self):
        self.counter = 0
        self.stack = []
        
    def ping(self, t: int) -> int:
        # We use a stack to keep track of the pings.
        # When we receive a ping, we add it to the stack and increment the counter.
        # We also remove any pings that are older than 3000 milliseconds.
        # Time complexity, O(n) : In the worst case, we may need to remove all elements from the stack
        # Space complexity, O(n) : In the worst case, we store all pings in the stack
        # Performance:
        # Runtime: faster than 60.98%
        # Memory Usage: less than 75.24%.
        self.stack.append(t)
        self.counter += 1

        while self.stack and (t - self.stack[0] > 3000):
            self.stack.pop(0)
            self.counter -= 1


        return self.counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
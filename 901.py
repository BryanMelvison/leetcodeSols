class StockSpanner:
    # So for this problem, I used a stack to keep track of the prices and the total number of days that the price was less than or equal to the current price. For each price, we pop from the stack until we find a price that is greater than the current price, and we add the total number of days that we popped to the total number of days for the current price.
    # This is quite neat to be honest, I think this compresses some of the redundant information, and make it efficient too
    # Time complexity, O(n) : Just one for loop
    # Space complexity, O(n) : store at most n elements in the stack
    # Performance:
    # Runtime: faster than 74.05%
    # Memory Usage: beats 73.31%.
    def __init__(self):
        self.result = []
        self.stack_total = []

    def next(self, price: int) -> int:
        total = 1
        while self.result and self.result[-1] <= price:
            self.result.pop(-1)
            total += self.stack_total.pop(-1)
        self.result.append(price)
        self.stack_total.append(total)
        return self.stack_total[-1]

        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
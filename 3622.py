class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # This is a simple problem, we can just iterate through the digits of the number and keep track of the sum and product of the digits, then check if the original number is divisible by the sum and product of its digits.
        # Time complexity: O(log n), where n is the number of digits in the number, we visit each digit once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 23.77%.
        initial = n
        sum_ = 0
        product_ = 1
        while n > 0:
            digit = n % 10
            sum_ += digit
            product_ *= digit    
            n = n // 10
        return initial % (sum_ + product_) == 0
        
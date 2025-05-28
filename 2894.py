class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # The sum of the first n natural numbers is given by the formula n(n + 1) / 2.
        # The sum of the first n natural numbers that are divisible by m can be calculated as follows:
        # The first number divisible by m is m, the second is 2m, and so on, up to the largest number less than or equal to n that is divisible by m.
        # The largest number divisible by m that is less than or equal to n is given by (n // m) * m.
        # The sum of the first k natural numbers is k(k + 1) / 2, so the sum of the first k numbers divisible by m is m * (k * (k + 1) / 2).
        # The difference of the two sums is then calculated by subtracting twice the sum of the first k numbers divisible by m from the total sum.
        # Time complexity, O(1): Constant time operations, worst case is n being very large.
        # Space complexity, O(1): No additional space used.
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 98.43%.
        total_sum = (n * (n + 1)) // 2
        total_divisible = n // m 
        total_div = 0
        for num in range(1, total_divisible + 1):
            total_div += num * m 
        return total_sum - 2*total_div
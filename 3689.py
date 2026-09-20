class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Calculate the maximum total value by taking the difference between the maximum and minimum elements in the list and multiplying by k
        # Find the maximum and minimum elements in the list
        # Time complexity: O(n), where n is the length of the nums list, we visit each element once to find the max and min.
        # Space complexity: O(1), we are using a constant amount of space to store the max and min values.
        # Performance:
        # Runtime: faster than 21.76%.
        # Memory Usage: less than 91.79%.
        return (max(nums) - min(nums))*k
class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        # Sort the list in descending order
        # Time complexity: O(n log n), where n is the length of the nums list, we sort the list.
        # Space complexity: O(1), we are using a constant amount of space to store
        # Performance:
        # Runtime: faster than 24.58%.
        # Memory Usage: less than 57.12%.
        nums.sort(reverse=True)
        print(nums)
        total = 0
        current = nums[0]
        for idx, num in enumerate(nums[1:], start = 1):
            if current != num:
                total += idx 
                current = num
        return total
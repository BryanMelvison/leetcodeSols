from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # This is a simple problem, we can just use two pointers to find the two numbers that add up to the target.
        # Time complexity: O(n), where n is the length of the numbers list, we
        # visit each element once.
        # Space complexity: O(1), we only use two pointers regardless of the input size.
        # Performance:
        # Runtime: faster than 79.64%.
        # Memory Usage: less than 76.68%.
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return []
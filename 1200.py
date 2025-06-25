from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the array first, then find the minimum difference between adjacent elements
        # Time complexity, O(n log n) : sorting the array
        # Space complexity, O(1) : we are not using any extra space except for the result
        # Performance:
        # Runtime: faster than 63.36%.
        # Memory Usage: less than 92.97%.
        arr.sort()
        global_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if global_diff > diff:
                global_diff = diff
        result = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == global_diff:
                result.append([arr[i], arr[i+1]])
        return result
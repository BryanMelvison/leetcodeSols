from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # This is a simple problem, we just need to find all combinations of k elements from n elements.
        # We can use recursion to find all combinations, and keep track of the current list.
        # Time complexity, O(n choose k) : n! / (k! * (n - k)!)
        # Space complexity, O(k) : We need to store the current list of k elements
        # Performance:
        # Runtime: faster than 14.31%.
        # Memory Usage: less than 87.75%.
        result = []
        def combination(currentList, start):
            if len(currentList) == k:
                result.append(currentList.copy()) #Give copy of the list
            for i in range(start, n + 1):
                currentList.append(i)
                combination(currentList, i + 1)
                currentList.pop()
        
        combination([], 1)
        return result
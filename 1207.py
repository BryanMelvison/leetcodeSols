from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # We can just keep track of the count of each element and then check if the counts are unique.
        # Time complexity, O(n) : Just one for loop to count and another to check uniqueness
        # Space complexity, O(n) : We are using a dictionary to store the counts
        # Performance:  
        # Runtime: faster than 100%
        # Memory Usage: less than 40.39%.
        from collections import Counter
        count = Counter(arr)

        dups = set()
        for key, value in count.items():
            if value not in dups:
                dups.add(value)
            else:
                return False
        return True
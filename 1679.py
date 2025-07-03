from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # We can use a dictionary to keep track of the numbers we have seen so far.
        # For each number, we check if the difference between k and the number is in the dictionary.
        # If it is, we can form a pair and increment the count.
        # Otherwise, we add the number to the dictionary.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : We are using a dictionary to store the numbers we have seen
        # Performance:
        # Runtime: faster than 78.91%
        # Memory Usage: less than 38.24%.
        store = {}
        total = 0
        for num in nums:
            diff = k - num
            if diff in store and store[diff] > 0:
                store[diff] -= 1
                total += 1
            else:
                store[num] = store.get(num, 0) + 1
        return total  

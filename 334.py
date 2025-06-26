from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # This is a simple problem, we just need to keep track of the first and second smallest elements in the array.
        # If we find a number greater than the second smallest, we have found a triplet.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : We are not using any extra space
        # Performance:
        # Runtime: faster than 99.6%.
        # Memory Usage: less than 99.98%.
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first: # Nums smaller than first, we update it
                first = num
            elif num <= second: # Else if there is a num bigger than first, smaller than second, update 
                second = num
            else: # Else if there is a num bigger than second, for sure its a triplet
                return True
        return False
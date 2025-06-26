import heapq
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        # use heap to sort 4 largest and 4 smallest items, why 4? consider case where we remove 3 directly from left/ right side, so we use array 4.
        # This method is efficient because it uses a heap to find the smallest and largest elements in the list, found from solution. 
        # Time complexity, O(n log k) : where n is the length of nums and k is the number of elements we want to find (4 in this case)
        # Space complexity, O(k) : we are using a heap of size k (4 in this case)
        # Performance:
        # Runtime: faster than 96%.
        # Memory Usage: less than 93.5%.
        smallest = heapq.nsmallest(4, nums)
        largest = heapq.nlargest(4, nums)
        
        return min(
            largest[0] - smallest[3],
            largest[1] - smallest[2],
            largest[2] - smallest[1],
            largest[3] - smallest[0]
        )
    
        # Sort the list first in ascending order, this was my attempt at solving the problem, I thought it would be easier to just sort the list and then find the minimum difference between the largest and smallest elements, but sorting
        # the list is not efficient enough for this problem, as it also sorts numbers that we don't need to consider.
        # if len(nums) <= 4:
        #     return 0
    
        # nums.sort()
        # Brute force way
        # return min([nums[-4] - nums[0], nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1]])

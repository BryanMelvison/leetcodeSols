from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # We can just convert the lists to sets and then find the difference
        # between the two sets. This will give us the unique elements in each list.
        # Time complexity, O(n + m) : where n and m are the lengths of the two lists
        # Space complexity, O(n + m) : we are using sets to store the unique elements
        # Performance:
        # Runtime: faster than 84.04%
        # Memory Usage: less than 90.50%.
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        temp = []
        for num in nums1:
            if num not in nums2:
                temp.append(num)
        res.append(temp)
        temp = []
        for num in nums2:
            if num not in nums1:
                temp.append(num)
        res.append(temp)
        return res
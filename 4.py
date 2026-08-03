from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # This problem is about finding the median of two sorted arrays. The approach I used is to combine both arrays into a single list, sort it, and then find the median based on the length of the combined list. If the length is even, the median is the average of the two middle elements; if it's odd, the median is the middle element.
        # Time complexity: O((m+n) log(m+n)) where m and n are the lengths of the two input arrays. This is due to the sorting step.
        # Space complexity: O(m+n) since we are creating a new list that contains all elements from both input arrays
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 95.12%.
        #find median index:
        total = nums1 + nums2
        total_len = len(total)
        total.sort()
        if total_len % 2 == 0:
            return (total[total_len// 2] + total[(total_len // 2) - 1]) / 2
        return total[total_len // 2]
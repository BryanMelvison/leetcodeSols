from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # So I used monolithic decreasing stack to keep track of numbers where they have not seen any higher numbers yet, once higher number is seen, we pop it from the stack to get the index, and store the number in a dict to get the next greater number for each number in nums2. Then we iterate through nums1 to get the next greater number for each number in nums1.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the stack
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 27.88%.

        # Since unique
        current = [-1] * len(nums2)
        stack = []
        for i in range(len(nums2)):
            while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop(-1)
                current[idx] = nums2[i]
            stack.append(i)

        temp = {}
        for idx, num in enumerate(nums2):
            temp[num] = current[idx]
        
        result = []
        for i in nums1:
            result.append(temp[i])
        return result
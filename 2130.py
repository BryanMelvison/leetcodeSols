# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Use multiple techniques to solve this problem:
        # 1. Fast and slow pointer to find the middle of the linked list.
        # 2. Reverse the second half of the linked list.
        # 3. Iterate through both halves to find the maximum twin sum.
        # Time complexity, O(n) : We traverse the linked list twice
        # Space complexity, O(1) : We use a constant amount of space
        # Performance:
        # Runtime: faster than 88.24%
        # Memory Usage: less than 65.88%.
        # Fast slow pointer to keep track of the second half
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse starting from slow (middle)
        current = slow
        prev = None
        while current:
            nextCurrent = current.next
            current.next = prev
            prev = current
            current = nextCurrent

        maxVal = 0
        while head and prev:
            maxVal = max(head.val + prev.val, maxVal)
            head = head.next
            prev = prev.next
        
        return maxVal
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We can reverse the linked list by iterating through it and reversing the pointers.
        # Time complexity, O(n) : We traverse the linked list once
        # Space complexity, O(1) : We use a constant amount of space
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 53.47%.
        # Base case
        if not head or not head.next:
            return head
        
        #else reverse
        prev = None
        current = head
        while current:
            # We keep track of next node:
            nextCurr = current.next
            # Reverse is done here,  set next to track previous, and previous to track current
            current.next = prev
            prev = current
            # Visual:
            # 1 (prev) -> 2 -> 3 -> 4
            # 1 (prev) -> 2 -> (nextCurr)...
            # 1 (prev) <- 2
            # 1 <- 2 (prev) --- (nextCurr)...
            # Continue again
            current = nextCurr
        return prev

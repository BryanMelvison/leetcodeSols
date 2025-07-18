from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Fast and Slow Pointers
        # We can use the fast and slow pointer technique to find the middle of the linked list.
        # We will also keep track of the previous node to delete the middle node.
        # Time complexity, O(n) : We traverse the linked list once
        # Space complexity, O(1) : We use a constant amount of space
        # Performance:
        # Runtime: faster than 47.69%
        # Memory Usage: less than 66.20%.
        if not head.next:
            return None
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head

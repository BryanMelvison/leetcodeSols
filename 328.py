from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We can use two pointers to separate the odd and even indexed nodes.
        # We will keep track of the head of the even indexed nodes to connect them at the end.
        # Time complexity, O(n) : We traverse the linked list once
        # Space complexity, O(1) : We use a constant amount of space
        # Performance:
        # Runtime: faster than 100.00%
        # Memory Usage: less than 94.14%.
        # This problem is about rearranging the linked list such that all odd indexed nodes come before even indexed nodes.
        # Base case: less than or equal to 2 nodes in total
        if not head or head.next == None or head.next.next == None:
            return head
        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

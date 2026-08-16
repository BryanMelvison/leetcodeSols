# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(val= -1, next =head)
        iter = result
        while iter and iter.next is not None:
            first = iter.next
            second = first.next
            if second: 
                first.next = second.next
                second.next = first 
                iter.next = second
            iter = first
        return result.next
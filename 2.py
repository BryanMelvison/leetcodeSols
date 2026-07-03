# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # just keep track of num not explored on both lists, if not explored pass in the diff between the numbers
        # Time complexity, O(max(m, n)) :  multiple for loops
        # Space complexity, O(max(m, n)) : array containing the excess water for each sweep (x2)

        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 10.78%.

        l_final = None
        l_result = None
        carry_over = 0
        while l1 and l2:
            total = l1.val + l2.val + carry_over
            value = total % 10
            carry_over = total // 10
            if l_final is None:
                l_final = ListNode(val = value)
                l_result = l_final
            else:
                l_final.next = ListNode(val = value) 
                l_final = l_final.next
            l1 = l1.next
            l2 = l2.next

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 +carry_over
            value = total % 10
            carry_over = total // 10
            l_final.next = ListNode(val = value) 
            l_final = l_final.next

            if l1: l1=l1.next
            if l2: l2=l2.next

        if carry_over != 0:
            l_final.next = ListNode(val = carry_over) 

        return l_result

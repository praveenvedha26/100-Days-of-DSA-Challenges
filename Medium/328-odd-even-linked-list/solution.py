# Problem 328: Odd Even Linked List
# Difficulty: Medium
# Link: https://leetcode.com/problems/odd-even-linked-list/
# Language: python3
# ────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd=head
        even=head.next
        even_head=head.next

        while (even!=None and even.next!=None):
            odd.next=odd.next.next
            even.next=even.next.next

            odd=odd.next
            even=even.next
        
        odd.next=even_head

        return head

        

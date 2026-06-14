# Problem 92: Reverse Linked List II
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-linked-list-ii/
# Language: python3
# ────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(-1,head)
        leftprev,curr=dummy,head
        for i in range(left-1):
            curr=curr.next
            leftprev=leftprev.next

        prev=None
        for i in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        leftprev.next.next=curr
        leftprev.next=prev

        return dummy.next
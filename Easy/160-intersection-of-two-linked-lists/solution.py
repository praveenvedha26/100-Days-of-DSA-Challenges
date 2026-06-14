# Problem 160: Intersection of Two Linked Lists
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Language: python3
# ────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1,temp2=headA,headB

        while temp1!=temp2:
            temp1=temp1.next
            temp2=temp2.next

            if temp1==temp2:
                return temp1

            if temp1==None: temp1=headB
            if temp2==None: temp2=headA

            
        return temp1
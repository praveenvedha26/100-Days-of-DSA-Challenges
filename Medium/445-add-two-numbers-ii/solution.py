# Problem 445: Add Two Numbers II
# Difficulty: Medium
# Link: https://leetcode.com/problems/add-two-numbers-ii/
# Language: python3
# ────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q1=[]
        q2=[]
        while l1 :
            if l1:
                q1.append(l1.val)
                l1=l1.next 
        while l2 :
            if l2: 
                q2.append(l2.val) 
                l2=l2.next
            
        carry=0
        head=None
        
        while q1 or q2 or carry:
            v1=q1.pop() if q1 else 0
            v2=q2.pop() if q2 else 0
            total=v1+v2+carry
            carry=total//10
            digit=total%10
            
            new_node=ListNode(digit)
            new_node.next=head
            head=new_node
        return head
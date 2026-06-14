# Problem 234: Palindrome Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/palindrome-linked-list/
# Language: python3
# ────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,newhead):
        prev=None
        while newhead:
            temp=newhead.next
            newhead.next=prev
            prev=newhead
            newhead=temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while (fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next

        secondhead=self.reverse(slow.next)
        
        while secondhead:
            if head.val!=secondhead.val:
                return False
            head=head.next
            secondhead=secondhead.next
        return True
    
    
    



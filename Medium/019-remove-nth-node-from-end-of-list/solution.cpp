# Problem 19: Remove Nth Node From End of List
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Language: cpp
# ────────────────────────────────────────

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode* thead=head;
        ListNode* curr=head;
        for(int i=0;i<n;i++){
            curr=curr->next;
        }
        if(curr==nullptr){
            return head->next;
        }
    
        while(curr->next!=nullptr){
            thead=thead->next;
            curr=curr->next;
        }
        thead->next=thead->next->next;
        return head;
    }
};
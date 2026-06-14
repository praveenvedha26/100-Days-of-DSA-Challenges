# Problem 143: Reorder List
# Difficulty: Medium
# Link: https://leetcode.com/problems/reorder-list/
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
    void reorderList(ListNode* head) {
        ListNode*dhead=head;
        ListNode*s=head;
        ListNode*f=head;
        while(f->next && f->next->next){
            f=f->next->next;
            s=s->next;
        }
        ListNode*prev=nullptr;
        ListNode*curr=s->next;
        s->next=nullptr;
        while(curr){
            ListNode*nextnode=curr->next;
            curr->next=prev;
            prev=curr;
            curr=nextnode;
        }
        ListNode* first = head;
        ListNode* second = prev;

        while (second) {
            ListNode* t1 = first->next;
            ListNode* t2 = second->next;

            first->next = second;
            second->next = t1;

            first = t1;
            second = t2;
        }
    }
};
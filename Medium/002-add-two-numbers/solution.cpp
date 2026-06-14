# Problem 2: Add Two Numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/add-two-numbers/
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode*l3=new ListNode(0);
        ListNode*ans=l3;
        int carry=0;
        int sum;
        while(l1||l2||carry){
            sum=carry;
            if(l1){
                sum=sum+l1->val;
                l1=l1->next;
            }
            if(l2){
                sum=sum+l2->val;
                l2=l2->next;
            }
            carry=sum/10;
            ListNode*Newnode=new ListNode(sum%10);
            l3->next=Newnode;
            l3=Newnode;
        }
        l3->next=nullptr;
        return ans->next;
    }
};
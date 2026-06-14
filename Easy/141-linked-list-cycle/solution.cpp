# Problem 141: Linked List Cycle
# Difficulty: Easy
# Link: https://leetcode.com/problems/linked-list-cycle/
# Language: cpp
# ────────────────────────────────────────

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*>stt;
        while(head!=nullptr){
            if(stt.find(head)!=stt.end()){
                return true;
            }
            stt.insert(head);
            head=head->next;
        }
        return false;
    }
};
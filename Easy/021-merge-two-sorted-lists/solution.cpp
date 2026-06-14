# Problem 21: Merge Two Sorted Lists
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* d = new ListNode(-1);
        ListNode* h = d;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                d->next = list1;
                list1 = list1->next;
            } else {
                d->next = list2;
                list2 = list2->next;
            }
            d = d->next;
        }

        // attach remaining list
        if (list1 ) {
            d->next = list1;
        } else {
            d->next = list2;
        }

        return h->next;
    }
};
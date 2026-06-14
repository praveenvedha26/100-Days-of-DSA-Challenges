# Problem 283: Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i,j;
        for (int i=0;i<nums.size();i++){
            if (nums[i]==0){
                j=i;
                break;
            }
        };
        for (int i=j+1;i<nums.size();i++){
            if (nums[i]!=0){
                swap(nums[i],nums[j]);
                j++;
            }
        };
    }
};
# Problem 152: Maximum Product Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-product-subarray/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int prod=1;
        int maxi=-10;
        for (int i=0;i<nums.size();i++){
            prod*=nums[i];
            maxi=max(maxi,prod);
            if (nums[i]==0){
                prod=1;
            }
        }
        prod=1;
        for (int i=nums.size()-1;i>=0;i--){
            prod*=nums[i];
            maxi=max(maxi,prod);
            if (nums[i]==0){
                prod=1;
            }
        }
        return maxi;
    }
};
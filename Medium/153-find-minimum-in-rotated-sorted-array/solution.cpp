# Problem 153: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int findMin(vector<int>& nums) {
        int low=0;
        int high=nums.size()-1;
        int lowestval=INT_MAX;
        while(low<=high){
            int mid = low + (high-low)/2;
            lowestval=min(lowestval,nums[mid]);

            if(nums[mid]>nums[high]){
                low=mid+1;
            }
            else {
                high=mid-1;
            }
            
        }
        return lowestval;
    }
};
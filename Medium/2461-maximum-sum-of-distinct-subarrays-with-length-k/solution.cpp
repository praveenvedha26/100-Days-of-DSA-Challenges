# Problem 2461: Maximum Sum of Distinct Subarrays With Length K
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        int i=0;
        int j=i+k-1;
        long long sum=0;
        long long maxi=0;
        unordered_map<int,int>mpp;
        for(int i=0;i<k;i++){
            mpp[nums[i]]++;
            sum+=nums[i];
        }
        while(j<nums.size()){
            if(mpp.size()==k){
                maxi=max(maxi,sum);
            }
            sum-=nums[i];
            mpp[nums[i]]--;
            if(mpp[nums[i]]<=0){
                mpp.erase(nums[i]);
            }
            i++;
            if(j<nums.size()){
                j++;
                if(j<nums.size()){
                    sum+=nums[j];
                    mpp[nums[j]]++;
                }
            }
        }
        return maxi;
    }
};
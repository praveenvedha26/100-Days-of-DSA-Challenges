# Problem 560: Subarray Sum Equals K
# Difficulty: Medium
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int>mpp;
        mpp[0]=1;
        int sum=0;
        int count=0;
        for (int i=0;i<nums.size();i++){
            sum=sum+nums[i];
            if (mpp.find(sum-k)!=mpp.end()){
                count+=mpp[sum-k];
            }
            mpp[sum]+=1;
        }
        return count;
    }
};
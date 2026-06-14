# Problem 15: 3Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/3sum/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;

        sort(nums.begin(), nums.end());

        int i = 0;
        int j = i + 1;
        int k = nums.size() - 1;

        while (i <= nums.size() - 3) {

            if (j >= k) {
                do { i++; } 
                while (i + 1 < nums.size() && nums[i] == nums[i-1]);

                j = i + 1;
                k = nums.size() - 1;
            }

            else if (nums[i] + nums[j] + nums[k] == 0) {

                ans.push_back({nums[i], nums[j], nums[k]});

                do { j++; } 
                while (j < k && nums[j] == nums[j-1]);

                do { k--; } 
                while (j < k && nums[k] == nums[k+1]);
            }

            else if (nums[i] + nums[j] + nums[k] < 0) {

                do { j++; } 
                while (j < k && nums[j] == nums[j-1]);

            }

            else {

                do { k--; } 
                while (j < k && nums[k] == nums[k+1]);

            }
        }

        return ans;
    }
};
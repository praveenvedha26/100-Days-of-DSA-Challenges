# Problem 11: Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0;
        int j=height.size()-1;
        int maxi=0;
        while(i<j){
            maxi=max(maxi,(j-i)*(min(height[i],height[j])));
            if(height[i]<height[j]) i++;
            else j--;
        }
        return maxi;
    }
};
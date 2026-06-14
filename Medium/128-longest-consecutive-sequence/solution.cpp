# Problem 128: Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size()==0){return 0;}
        int c=0;
        int maxi=INT_MIN;
        unordered_set<int>stt(nums.begin(),nums.end());
        for (auto itt=stt.begin();itt!=stt.end();itt++){
            if (stt.find(*itt-1)!=stt.end()){
                c=0;
                continue;
            }
            else{
                c=1;
                int val=*itt;
                while(stt.find(val+1)!=stt.end()){
                    val+=1;
                    c++;
                }
            }
            maxi=max(maxi,c);
        }
        return maxi;
    }
};
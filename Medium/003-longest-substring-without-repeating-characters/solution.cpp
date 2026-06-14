# Problem 3: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i=0;
        int maxi=0;
        unordered_map<char,int>mpp;
        for(int j=0;j<s.size();j++){
            mpp[s[j]]++;
            if(mpp.size()==j-i+1){
                
                maxi=max(maxi,j-i+1);
            }
            else{
                mpp[s[i]]--;
                if(mpp[s[i]]<=0){
                    mpp.erase(s[i]);
                }
                i++;
                
            }
        }
        return maxi;
    }
};
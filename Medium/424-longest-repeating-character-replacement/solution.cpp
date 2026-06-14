# Problem 424: Longest Repeating Character Replacement
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int characterReplacement(string s, int k) {
        int i=0;
        int maxi=0;
        int maxf=0;
        
        unordered_map<char,int>mpp;
        for(int j=0;j<s.size();j++){
            mpp[s[j]]++;
            maxf=0;
            for(auto &itt:mpp){
                maxf=max(maxf,itt.second);
            }
            if((j-i+1)-maxf<=k){
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
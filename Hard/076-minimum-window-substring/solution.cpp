# Problem 76: Minimum Window Substring
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-window-substring/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char,int>mpp;
        for(int i=0;i<t.size();i++){
            mpp[t[i]]++;
        }
        int c=0;
        int mini=INT_MAX;
        int i=0;
        int st=-1;
        for(int j=0;j<s.size();j++){
            if(mpp[s[j]]>0){
                c++;
            }
            mpp[s[j]]--;
            while(c==t.size()){
                mpp[s[i]]++;
                if(mpp[s[i]]>0){
                    c--;
                }
                if(mini>j-i+1){
                    mini=j-i+1;
                    st=i;
                }
                i++;
            }
        }
        if(st==-1){return "";}
        return s.substr(st,mini);
        
    }
};
# Problem 739: Daily Temperatures
# Difficulty: Medium
# Link: https://leetcode.com/problems/daily-temperatures/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int>st;
        vector<int>res;
        for(int i=temperatures.size()-1;i>=0;i--){
            while(!st.empty()&&temperatures[st.top()]<=temperatures[i]){
                st.pop();
            }
            if(st.empty()){
                st.push(i);
                res.push_back(0);
            }
            else{
                res.push_back(st.top()-i);
                st.push(i);
            }
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
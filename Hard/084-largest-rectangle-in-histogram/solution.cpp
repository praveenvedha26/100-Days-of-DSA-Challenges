# Problem 84: Largest Rectangle in Histogram
# Difficulty: Hard
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int>st;
        long long maxi=0;
        for(int i=0;i<heights.size();i++){
            while(!st.empty() && heights[st.top()]>heights[i]){
                long long ele=st.top();
                st.pop();
                long long width=i-(st.empty() ? -1 : st.top())-1;
                maxi=max(maxi,heights[ele]*(width));
            }
            st.push(i);
        }
        while(!st.empty()){
            long long i=heights.size();
            long long ele=st.top();
            st.pop();
            long long width=i-(st.empty() ? -1 : st.top())-1;
            maxi=max(maxi,heights[ele]*(width));;
        }
        return maxi;
    }
};
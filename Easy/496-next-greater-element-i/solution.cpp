# Problem 496: Next Greater Element I
# Difficulty: Easy
# Link: https://leetcode.com/problems/next-greater-element-i/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int>st;
        unordered_map<int,int>res;
        for(int i=nums2.size()-1;i>=0;i--){
            while(!st.empty()&&nums2[st.top()]<=nums2[i]){
                st.pop();
            }
            if(st.empty()){
                st.push(i);
                res[nums2[i]]=-1;
            }
            else{
                res[nums2[i]]=nums2[st.top()];
                st.push(i);
            }
        }
        vector<int>ans;
        for(auto itt:nums1){
            ans.push_back(res[itt]);
        }
        return ans;
    }
};
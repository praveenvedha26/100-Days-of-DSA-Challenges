# Problem 20: Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    bool isValid(string s) {
        stack<int>st;
        int o=0;
        int c=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
                st.push(')');
                o++;
            }
            else if(s[i]=='['){
                st.push(']');
                o++;
            }
            else if(s[i]=='{'){
                st.push('}');
                o++;
            }
            else{
                if(!st.empty() && st.top()==s[i]){
                    st.pop();
                }
                else{
                    return false;
                }
                c++;
            }
        }
        if(o!=c){
            return false;
        }
        return true;
    }
};
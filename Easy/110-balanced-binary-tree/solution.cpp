# Problem 110: Balanced Binary Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Language: cpp
# ────────────────────────────────────────

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        int height = heightofbt(root);
        if(height==-1){return false;}
        return true;
    }
    int heightofbt(TreeNode*root){
        if(root==NULL){return 0;}

        int lh = heightofbt(root->left);
        if(lh==-1){return -1;}
        int rh = heightofbt(root->right);
        if(rh==-1){return -1;}
        
        if(abs(lh-rh)>1){return -1;}
        
        
        return (1+max(lh,rh));
    }
};
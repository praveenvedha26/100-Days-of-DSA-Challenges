# Problem 145: Binary Tree Postorder Traversal
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
# Language: python3
# ────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def postorder(node,res):
            if node:
                postorder(node.left,res)
                postorder(node.right,res)
                res.append(node.val)
                
        postorder(root,res)
        return res
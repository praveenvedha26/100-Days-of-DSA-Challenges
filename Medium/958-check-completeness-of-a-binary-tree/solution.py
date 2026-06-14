# Problem 958: Check Completeness of a Binary Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# Language: python3
# ────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        Q=collections.deque()
        Q.append(root)
        flag=False
        while Q:
            node=Q.popleft()
            if not node:
                flag=True
            else:
                if flag==True:
                    return False
                Q.append(node.left)
                Q.append(node.right)
            
        return True
        
# Problem 102: Binary Tree Level Order Traversal
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Language: python3
# ────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return[]
        res=[]
        Q=collections.deque()
        Q.append(root)
        while Q:
            size=len(Q)
            lst=[]
            for i in range(0,size):
                node=Q.popleft()
                lst.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right: 
                    Q.append(node.right)
                
            res.append(lst)

        return res
# Problem 623: Add One Row to Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/add-one-row-to-tree/
# Language: python3
# ────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            l=TreeNode(val)
            l.left=root
            return l
        Q=collections.deque()
        Q.append(root)
        c=1
        while Q:
            if c+1==depth:
                for i in range(len(Q)):
                    node=Q.popleft()
                    l=TreeNode(val)
                    r=TreeNode(val)
                    if node.left:
                        l.left=node.left
                    if node.right:
                        r.right=node.right
                    node.left=l
                    node.right=r
                break
            for i in range(len(Q)):
                node=Q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)    
            c+=1    
        return root
# Problem 108: Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Language: python3
# ────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,nums,L,R):
        if L>R:
            return None
        index=((R-L)//2)+((R-L)%2)+L
        NewNode=TreeNode(nums[index])
        NewNode.left=self.dfs(nums,L,index-1)
        NewNode.right=self.dfs(nums,index+1,R)
        return NewNode

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums,0,len(nums)-1)

        
# Problem 331: Verify Preorder Serialization of a Binary Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        space=1
        if preorder[0]=="#" and len(preorder)==1:
            return True
        if preorder[0]=="#":
            return False
        for i in preorder.split(","):
            space-=1
            if space<0:
                return False        
            if i!="#":
                space+=2
        if space==0:
            return True
        return False
            
        
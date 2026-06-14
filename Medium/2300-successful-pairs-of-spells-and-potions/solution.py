# Problem 2300: Successful Pairs of Spells and Potions
# Difficulty: Medium
# Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        for s in spells:
            l,r=0,len(potions)-1
            index=len(potions)
            while l<=r:
                m=(l+r)//2
                if potions[m]*s>=success:
                    r=m-1
                    index=m
                else:
                    l=m+1
            
            res.append(len(potions)-index)
        return res


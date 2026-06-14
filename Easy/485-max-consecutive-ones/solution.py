# Problem 485: Max Consecutive Ones
# Difficulty: Easy
# Link: https://leetcode.com/problems/max-consecutive-ones/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res,count=0,0
        for i in nums:
            if i==1:
                count+=1
            else:
                count=0
            res=max(res,count)
        return res
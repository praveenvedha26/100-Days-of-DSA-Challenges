# Problem 2348: Number of Zero-Filled Subarrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i,res=0,0
        while i<len(nums):
            count=0
            while i<len(nums) and nums[i]==0:
                i+=1
                count+=1
                res+=count
            i+=1
        return res

                                                



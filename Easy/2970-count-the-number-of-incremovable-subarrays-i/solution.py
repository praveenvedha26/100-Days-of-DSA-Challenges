# Problem 2970: Count the Number of Incremovable Subarrays I
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if self.subarray(i,j,nums):
                    count+=1
        return count

    def subarray(self,start,end,nums):
        prev= float('-inf')
        for i in range(len(nums)):
            if i<=end and i>=start:
                continue
            if nums[i]<=prev:
                return False
            prev=nums[i]
        return True
        
        
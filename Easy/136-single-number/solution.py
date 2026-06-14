# Problem 136: Single Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/single-number/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary={}
        for i in nums:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]=dictionary[i]+1
                
        for key in dictionary.keys():
            if dictionary[key]==1:
                return key
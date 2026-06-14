# Problem 1929: Concatenation of Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/concatenation-of-array/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums
        def concatenation(ans,nums):
            ans+=nums
            return ans
        concatenation(ans,nums)
        return ans
# Problem 2439: Minimize Maximum of Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimize-maximum-of-array/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = tot = nums[0]

        for i in range(1,len(nums)):
            tot+=nums[i]
            new=math.ceil(tot/(i+1))
            res=max(res,new)
        return res
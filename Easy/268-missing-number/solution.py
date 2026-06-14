# Problem 268: Missing Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/missing-number/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            if i==nums[i]:
                i+=1
            else:
                return i
        return len(nums)

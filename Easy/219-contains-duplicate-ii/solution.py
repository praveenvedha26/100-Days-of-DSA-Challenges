# Problem 219: Contains Duplicate II
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate-ii/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D={}
        for i in range(len(nums)):
            if nums[i] in D and (i-D[nums[i]]<=k):
                return True
                break
            D[nums[i]]=i
        return False
# Problem 594: Longest Harmonious Subsequence
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-harmonious-subsequence/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        nums1=list(set(nums))
        nums1.sort()
        maxi=0
        for i in range(len(nums1)-1):
            if nums1[i+1]-nums1[i]==1:
                sum=d[nums1[i+1]]+d[nums1[i]]
                maxi=max(sum,maxi)
        return maxi
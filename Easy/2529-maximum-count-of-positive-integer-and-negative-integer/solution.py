# Problem 2529: Maximum Count of Positive Integer and Negative Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0)  # First index where num >= 0
        pos = len(nums) - bisect_right(nums, 0)  # First index where num > 0
        return max(neg, pos)
# Problem 189: Rotate Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-array/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k!=0:
            new=nums.pop(-1)
            nums.insert(0,new)
            k-=1
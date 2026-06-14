# Problem 34: Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      
        res = [-1, -1]

        def expandFromMid(nums, mid):
            l, r = mid, mid
            while l > 0 and nums[l-1] == target:
                l -= 1
            while r < len(nums) - 1 and nums[r+1] == target:
                r += 1
            return l, r

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                l, r = expandFromMid(nums, mid)
                res[0], res[1] = l, r
                return res
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return res

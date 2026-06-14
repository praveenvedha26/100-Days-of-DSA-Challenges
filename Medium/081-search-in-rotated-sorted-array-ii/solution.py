# Problem 81: Search in Rotated Sorted Array II
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,h=0,len(nums)-1

        while l<=h:
            m=(l+h)//2

            if nums[m]==target:
                return True
            
            if nums[l]==nums[m]==nums[h]:
                l+=1
                h-=1
            else:
                if nums[l]<=nums[m]:
                    if nums[l]<=target and target<=nums[m]:
                        h=m-1
                    else:
                        l=m+1
                elif nums[m]<=nums[h]:
                    if nums[m]<=target<=nums[h]:
                        l=m+1
                    else:
                        h=m-1
            
        return False
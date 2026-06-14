# Problem 2405: Optimal Partition of String
# Difficulty: Medium
# Link: https://leetcode.com/problems/optimal-partition-of-string/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def partitionString(self, s: str) -> int:
        hash=set()
        res=1
        for i in s:
            if i in hash:
                res+=1
                hash=set()
            hash.add(i)
        return res
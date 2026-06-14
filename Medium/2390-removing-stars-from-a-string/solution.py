# Problem 2390: Removing Stars From a String
# Difficulty: Medium
# Link: https://leetcode.com/problems/removing-stars-from-a-string/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def removeStars(self, s: str) -> str:
        
        Q=collections.deque()
        for i in s:
            if i!="*":
                Q.append(i)
            if i=="*":
                Q.pop()
        
        return (''.join(Q))
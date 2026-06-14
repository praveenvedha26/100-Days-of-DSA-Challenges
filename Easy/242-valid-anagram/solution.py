# Problem 242: Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans1=sorted(s)
        ans2=sorted(t)
        if ans1==ans2:
            return True
        return False
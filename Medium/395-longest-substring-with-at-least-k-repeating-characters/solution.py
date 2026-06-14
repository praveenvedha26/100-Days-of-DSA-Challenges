# Problem 395: Longest Substring with At Least K Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        from collections import Counter
        freq = Counter(s)

        for mid in range(len(s)):
            if freq[s[mid]] < k:
                left = self.longestSubstring(s[:mid], k)
                right = self.longestSubstring(s[mid + 1:], k)
                return max(left, right)

        return len(s)

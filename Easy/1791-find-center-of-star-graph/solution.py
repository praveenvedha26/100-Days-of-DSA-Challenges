# Problem 1791: Find Center of Star Graph
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-center-of-star-graph/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u) 
        max_key=max(adj,key=lambda k:len(adj[k]))
        return max_key
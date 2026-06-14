# Problem 1971: Find if Path Exists in Graph
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited=set()
        neighbours=defaultdict(list)
        for u,v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
        
        def dfs(i):
            if i==destination:
                return True
            for neighbour in neighbours[i]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if dfs(neighbour):
                        return True
            return False        
        return dfs(source)
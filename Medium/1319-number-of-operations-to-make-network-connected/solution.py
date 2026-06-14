# Problem 1319: Number of Operations to Make Network Connected
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        neighbor=[set() for i in range(n)]

        for u,v in connections:
            neighbor[u].add(v)
            neighbor[v].add(u)
            
        visited=[0]*n

        def dfs(node):
            if visited[node]:
                return 0

            visited[node]=1

            for nei in neighbor[node]:
                dfs(nei)
                
            return 1
        
        return sum(dfs(i) for i in range(n))-1
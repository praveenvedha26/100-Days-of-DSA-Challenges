# Problem 547: Number of Provinces
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-provinces/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        province=0
        visited=[False]*n
        
        def dfs(node):
            visited[node]=True
            for neighbour in range(n):
                if isConnected[node][neighbour]==1 and not visited[neighbour]:
                    dfs(neighbour)

        for i in range (n):
            if not visited[i]:
                dfs(i)
                province+=1
        return province
# Problem 802: Find Eventual Safe States
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-eventual-safe-states/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        safe={}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False
            for neighbour in graph[i]:
                if not dfs(neighbour):
                    return False
            safe[i]=True
            return True

        res=[]
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

        
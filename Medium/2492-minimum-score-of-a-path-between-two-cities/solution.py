# Problem 2492: Minimum Score of a Path Between Two Cities
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        path=defaultdict(list)
        for src,dst,dist in roads:
            path[src].append((dist,dst))
            path[dst].append((dist,src))
        
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            nonlocal res
            for dist,dst in path[i]:
                res=min(res,dist)
                dfs(dst)

        res=float(inf)
        visit=set()
        dfs(1)
        return res
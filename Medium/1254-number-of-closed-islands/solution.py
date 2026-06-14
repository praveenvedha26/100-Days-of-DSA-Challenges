# Problem 1254: Number of Closed Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-closed-islands/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        visit=set()

        def dfs(r,c):
            if (r<0) or (c<0) or (r==ROW) or (c==COL):
                return 0

            if (grid[r][c]==1) or ((r,c) in visit):
                return 1

            visit.add((r,c))
            return min(dfs(r+1,c),
                       dfs(r-1,c),
                       dfs(r,c+1),
                       dfs(r,c-1))            

        res=0
        for r in range(ROW):
            for c in range(COL):
                if not grid[r][c] and (r,c) not in visit:
                    res+=dfs(r,c)

        return res
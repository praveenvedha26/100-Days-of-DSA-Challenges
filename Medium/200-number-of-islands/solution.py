# Problem 200: Number of Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-islands/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visited=set()
        island=0

        def bfs(r,c):
            Q=collections.deque()
            visited.add((r,c))
            Q.append((r,c))
            while Q:
                row,col=Q.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if ((nr in range(rows)) and (nc in range(cols)) and grid[nr][nc]=="1" and (nr,nc)not in visited):
                        Q.append((nr,nc))
                        visited.add((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c)not in visited:
                    bfs(r,c)
                    island+=1
        return island
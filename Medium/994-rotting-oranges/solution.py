# Problem 994: Rotting Oranges
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotting-oranges/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time,fresh=0,0
        r=len(grid)
        c=len(grid[0])
        Q=collections.deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    Q.append((i,j))
        while Q and fresh>0:
            for k in range(len(Q)):

                row,col=Q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if nr not in range(r) or nc not in range(c) or grid[nr][nc]!=1:
                        continue
                    grid[nr][nc]=2
                    Q.append((nr,nc))
                    fresh-=1
            time+=1 
        return time if fresh==0 else -1
        